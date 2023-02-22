# chatgpt.py
import sys
# import imp
import importlib.util

sys.path.append('/Users/carlos/Downloads/chatgpt-wrapper/chatgpt_wrapper')

# from chatgpt import ChatGPT

# ChatGPT = imp.load_source('ChatGPT', '/Users/carlos/Downloads/chatgpt-wrapper/chatgpt_wrapper/chatgpt.py')

spec = importlib.util.spec_from_file_location('ChatGPT', '/Users/carlos/Downloads/chatgpt-wrapper/chatgpt_wrapper/chatgpt.py')
chatgpt_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(chatgpt_module)

print("chatgpt module is:{0}".format(chatgpt_module.ChatGPT))

ChatGPT = chatgpt_module.ChatGPT

if __name__ == "__main__":
    bot = None
    if bot == None:
        bot = ChatGPT()

    print("chatgpt bot is:{0}".format(bot))

    response = bot.ask("what is sum of 1+2 ")

    print("response is: {0}".format(response))
