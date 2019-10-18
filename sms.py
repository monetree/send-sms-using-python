from twilio.rest import Client

#following details you can find from twilio account.
accout_sid = 'your_accout_sid'
auth_token = 'your_auth_token'

client = Client(accout_sid, auth_token)

#below numbers used for message are just random numbers
message = client.messages.create(
        from_= '+918000802869',
        body='I CANT BELIVE THIS WORKS',
        to='+7008604545'
    )

print(message.sid)