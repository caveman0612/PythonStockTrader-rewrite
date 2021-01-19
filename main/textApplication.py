from twilio.rest import Client
from passwords import *



def sendTextMessage(message):

    # Your Account SID from twilio.com/console

    # Your Auth Token from twilio.com/console


    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+12182521896",
        from_="+12014743471",
        body=message)

# sendTextMessage("test")