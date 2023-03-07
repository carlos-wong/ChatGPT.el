# chatgpt.py
import sys

sys.path.insert(0, '/Users/carlos/Downloads/chatgpt-wrapper')

from epc.server import EPCServer
from chatgpt_wrapper import ChatGPT

server = EPCServer(('localhost', 0))

bot = None
stringbot = None

def get_cahtgpt_bot():
    global bot
    if bot == None:
        bot = ChatGPT()

@server.register_function
def query(query):
    global bot
    get_cahtgpt_bot()
    return bot.ask(query)

@server.register_function
def querystream(query):
    global bot
    get_cahtgpt_bot()
    global stringbot
    if stringbot == None:
        stringbot = iter(bot.ask_stream(query))

    try:
        return next(stringbot)
    except StopIteration:
        stringbot = None
        return None

@server.register_function
def switch_to_chat(chat_uuid):
    global bot
    get_cahtgpt_bot()
    # bot.switch_to_conversation(chat_uuid)
    return ""

server.print_port()
server.serve_forever()
