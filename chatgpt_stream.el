;;; --- Buffer for first time use code -*- lexical-binding: t; -*-
(defun chatgpt--query-stream (query &optional recursive)
  (unless chatgpt-process
    (chatgpt-init))
  (let ((next-query query)
        (saved-id (if recursive
                      chatgpt-id
                    (cl-incf chatgpt-id)))
        (next-recursive recursive))

    (if (not recursive)
        (progn
          (chatgpt--insert-query query saved-id)
          (chatgpt-display)))

    (deferred:$
     (deferred:$
      (epc:call-deferred chatgpt-process 'querystream (list query))
      (deferred:nextc it
                      #'(lambda (response)
                          (with-current-buffer (chatgpt-get-filename-buffer)
                            (save-excursion
                              (if (numberp next-recursive)
                                  (goto-char next-recursive)
                                (progn
                                  (chatgpt--goto-identifier chatgpt-id)
                                  (chatgpt--clear-line)))
                              (if (and (stringp response))
                                  (progn
                                    (with-silent-modifications
                                      (insert response))
                                    (chatgpt--query-stream next-query (point)))
                                (progn
                                  (with-silent-modifications
                                    (insert (format "\n\n%s END %s"
                                                    (make-string 30 ?=)
                                                    (make-string 30 ?=))))
                                  (and chatgpt-finish-response-hook (run-hooks 'chatgpt-finish-response-hook)))))))))
     (deferred:error it
                     `(lambda (err)
                        (message "err is:%s" err))))))

(defun chatgpt--query-by-type-stream (query query-type)
  (if (equal query-type "custom")
      (chatgpt--query
       (format "%s\n\n%s" (read-from-minibuffer "ChatGPT Custom Prompt: ") query))
    (if-let (format-string (cdr (assoc query-type chatgpt-query-format-string-map)))
        (chatgpt--query-stream
         (format format-string query))
      (error "No format string associated with 'query-type' %s. Please customize 'chatgpt-query-format-string-map'" query-type))))

(defun chatgpt-query-by-type-stream (query)
  (interactive (list (if (region-active-p)
                         (buffer-substring-no-properties (region-beginning) (region-end))
                       (read-from-minibuffer "ChatGPT Stream Query: "))))
  (let* ((query-type (completing-read "Type of Stream Query: " (cons "custom" (mapcar #'car chatgpt-query-format-string-map)))))
    (if (or (assoc query-type chatgpt-query-format-string-map)
            (equal query-type "custom"))
        (chatgpt--query-by-type-stream query query-type)
      (chatgpt--query-stream (format "%s\n\n%s" query-type query)))))

(defun chatgpt-query-stream (query)
  (interactive (list (if (region-active-p)
                         (buffer-substring-no-properties (region-beginning) (region-end))
                       (read-from-minibuffer "ChatGPT Stream Query: "))))
  (if (region-active-p)
      (chatgpt-query-by-type-stream query)
    (chatgpt--query-stream query)))

(provide 'chatgpt_stream)
