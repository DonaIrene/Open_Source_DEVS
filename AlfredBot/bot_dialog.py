#Flask, Twilio required
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.twiml import Client


#pip install chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


class user_whats:
    app = Flask(__name__)

    @app.route("/bot", methods=['POST'])

    def bot():
        incoming_msg = request.values.get('Body', '').lower()
        resp = MessagingResponse()
        msg = resp.message()
        responded = False  

class bot_alfred:
    bot = ChatBot(
        'Alfred',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        logic_adapters =[
            'chatterbot.logic.MathematicalEvaluation',
            'chatterbot.logic.TimeLogicAdapter',
            'chatterbot.logic.BestMatch'
            ],
            database_uri = 'sqlite:///database.db'
    )
    treiner = ListTrainer(bot)

    treiner.train = ([
        'Oi',
        'Tudo bem?',
        'Sim e com você?',
        'Ainda Bem, é bom ouvir isso!'])

    while True :
        try:
            user_input = user_whats()
            bot_Input = bot.get_response()
        except (KeyboardInterrupt,EOFError,SystemError):
            break

    response = bot.get_response('')
