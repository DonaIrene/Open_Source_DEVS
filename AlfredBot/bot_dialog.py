from urllib import response
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


class bot_alfred:
    bot = ChatBot('Alfred',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters =[{
    'defeault_response':"Desculpa, mas ainda nao percebo sobre esse assunto.",
    'maximum_similarity_threshold':0.80}
    ],
    database_uri = 'sqlite:///database.sqlite3'
    )
    treiner = ListTrainer(bot)

    treiner.train = ([
        'Oi',
        'Tudo bem?',
        'Sim e com você?',
        'Ainda Bem, é bom ouvir isso!'])

    while True :
        try:
            bot_Input = bot.get_response()
        except (KeyboardInterrupt,EOFError,SystemError):
            break

    response = bot.get_response()
