from twilio.rest import Client

# Twilio credentials
account_sid = 'ACf57012fefcc2d9d8e24db3e45aab0efe'  # Get from Twilio console
auth_token = '7a828db808b7fbec4d7318a6e93be363'  # Get from Twilio console

client = Client(account_sid, auth_token)

message = client.messages.create(
    body='Poaching activity detected!',
    from_='+17756406408',  # Your Twilio number
    to='+918778244247'  # Your phone number
)

print(f"Message sent with SID: {message.sid}")
