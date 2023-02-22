# chatgpt.py

from epc.server import EPCServer
from chatgpt_wrapper import ChatGPT

server = EPCServer(('localhost', 0))

bot = None
stringbot = None

@server.register_function
def query(query):
    global bot
    if bot == None:
        bot = ChatGPT()
    return bot.ask(query)

@server.register_function
def querystream(query):
    global bot
    if bot == None:
        bot = ChatGPT()

    global stringbot
    if stringbot == None:
        stringbot = iter(bot.ask_stream(query))

    try:
        return next(stringbot)
    except StopIteration:
        stringbot = None
        return None


server.print_port()
server.serve_forever()
