from twilio.rest import TwilioRestClient

# Your can find your AccountSID and AuthToken from http://twilio.com/user/account
account_sid = "ACddff8abf96eceac108145325a53b0133" #Replace this with your account ID
auth_token = "05cad309cd5bf50f2a5cb5162010e205" #Replacet his with your Auth Token
client = TwilioRestClient(account_sid, auth_token)

call = client.calls.create(to="+13025357797", #Replace this with the phone number you wish to recieve calls at
                           from_="+13023172180", #Replace this with the phone number Twilio assigned to you
                           url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")
print "making a call to 302-535-7797"