##Imports##
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

 


#APP#
app = Flask (__name__)

@app.route("/bot", methods=['POST'])

def bot():
    #add webhook logic here and return a response
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False


    if 'citacao' in incoming_msg:
        #resposta#
        r = request.get('')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else: 
            quote = 'Nao foi possivel encontrar uma citacao, desculpa'
        msg.body(quote)    
        responded = True

    if 'gato' in incoming_msg or 'gata' in incoming_msg:
        msg.media('https://cataas.com/cat')
        responded = True

    if not responded:
        #resposta caso negativo
        msg.body('So conheco frases e gatos famosos!')

    return str (resp)

        

if __name__ == '__main__':
   app.run()