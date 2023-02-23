# chatgpt.py
import sys
import datetime
import importlib

# import imp

sys.path.insert(0, '/Users/carlos/Downloads/chatgpt-wrapper')

from chatgpt_wrapper.chatgpt import ChatGPT

# from chatgpt import ChatGPT

# ChatGPT = imp.load_source('ChatGPT', '/Users/carlos/Downloads/chatgpt-wrapper/chatgpt_wrapper/chatgpt.py')

# spec = importlib.util.spec_from_file_location('ChatGPT', '/Users/carlos/Downloads/chatgpt-wrapper/chatgpt_wrapper/chatgpt.py')
# chatgpt_module = importlib.util.module_from_spec(spec)
# spec.loader.exec_module(chatgpt_module)

# print("chatgpt module is:{0}".format(chatgpt_module.ChatGPT))

# ChatGPT = chatgpt_module.ChatGPT


bot = None
if bot == None:
    bot = ChatGPT(headless = False)

print("chatgpt bot is:{0}".format(bot))
# bot.select_conversation_id("b912cdb8-a77e-4932-8f65-6e800b654098")
# bot.set_conversation_id_parent_message_id("e6db6053-ae64-410f-b979-02fc24b8ad55","a251de7d-e536-49c2-8a42-25f6fce7409f")
# response = bot.ask("what is sum of 1+2 ")

global conversation_info

# conversation_info =  bot.get_conversation_info("e6db6053-ae64-410f-b979-02fc24b8ad55")

bot.switch_to_conversation("e6db6053-ae64-410f-b979-02fc24b8ad55")

# print("response is: {0}".format(response))
# response = bot.ask("not it is 4 ")

# print("response is: {0}".format(response))

current_time = datetime.datetime.now();formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

response = bot.ask("sorry it is 3 and now is:{0}".format(formatted_time))

print("response is: {0}".format(response))
# input_result = input("Press Enter to continue...")
import code; code.interact(local=locals())
