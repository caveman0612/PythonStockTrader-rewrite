from twilio.rest import Client



def sendTextMessage(message):

    # Your Account SID from twilio.com/console
    account_sid = "AC5dd1e1c5f305b831f9b1befedd9541ba"
    # Your Auth Token from twilio.com/console
    auth_token = "7924082ef8cb7b6b203c5d4afe38a4e4"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+12182521896",
        from_="+12014743471",
        body=message)

# sendTextMessage("test")