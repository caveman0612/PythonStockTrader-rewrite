from twilio.rest import Client
from passwords import account_sid, auth_token

# imported account_sid, auth_token from passwords

### Main functions ###__________________________________________________

def sendTextMessage(message):

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to="+12182521896",
        from_="+12014743471",
        body=message)








