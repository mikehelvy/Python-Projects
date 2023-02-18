from twilio.rest import Client
import keys

client = Client (keys.account_sid, keys.auth_token)

message = client.messages.create(
  body="This message is from your nerdy husband learning to code!",
  from_=keys.twilio_number,
  to=keys.target_number
  ) 

print(message.body)