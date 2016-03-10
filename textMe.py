from twilio.rest import TwilioRestClient

# put your own credentials here
ACCOUNT_SID = "ACddff8abf96eceac108145325a53b0133"
AUTH_TOKEN = "05cad309cd5bf50f2a5cb5162010e205"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

client.messages.create(
	to="13025357797",
	from_="+13023172180",
	body="secretvolumeup",
)

print "texted 302-535-7797 to turn up phone volume."