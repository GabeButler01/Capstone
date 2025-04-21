# Download the helper library from https://www.twilio.com/docs/python/install
import os
import time
import itertools
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "████████████████████████████████" # Account SID (use secrets file)
auth_token = "████████████████████████████████" # Auth Token (use secrets file)
client = Client(account_sid, auth_token)

# list of voicemails recordings

voicemails = ["https://capstonephone-1326.twil.io/Dad%20line%206%20NEW.wav",
              "https://capstonephone-1326.twil.io/Friend%202%20line%206%20NEW.wav",
              "https://capstonephone-1326.twil.io/Sister%20line%207%20NEW.wav",
              "https://capstonephone-1326.twil.io/Friend1Line6.wav",
              "https://capstonephone-1326.twil.io/Dad%20line%207%20NEW.wav",
              "https://capstonephone-1326.twil.io/Friend1Line7.wav"
            ]

# cycle through the list and play a voicemail every minute (press ctrl + c is stop infinite loop)
for item in itertools.cycle(voicemails):
    call = client.calls.create(
        from_="████████████", # generated twilio phone number
        to="████████████", # personal phone number (connected to rotary phone)
        url = item
    )
    time.sleep(120)

print(call.sid)
