from twilio.rest import Client

# put your own credentials here
ACCOUNT_SID = "ACbd4e2d982488770e53f7aad9c998681a"
AUTH_TOKEN = "4b4e4074817986e25aeec5f9eae6fe88"

client = Client(ACCOUNT_SID, AUTH_TOKEN)


#  send SMS
message = client.messages.create(from_="+48799449209",
                                 to="+359898776643",
                                 body="Hi from Python")
print(message.sid)

# make a call
call = client.calls.create(from_="+48799449209",
                           to="+359898776643",
                           url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")
print(call.sid)
