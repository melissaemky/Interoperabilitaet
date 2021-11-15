import RPi.GPIO as GPIO
import os
from  twilio.rest import Client

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN)

ACCOUNT_SID = 'AC3b9a640bf840e9f26596a841e249f686'
AUTH_TOKEN = 'fdf9ae04ae3555c0dbd08aed5e1eec31'
FROM = '+14155238886'
TO = '+4915770217327'

# Endlosschleife
while True:
    if GPIO.input(16) == 0:
        print("!!!Hausnotrum ALARM!!!")
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        client.message.create(
            to=TO
            from_=FROM,
            body="!!!Hausnotrum ALARM!!!")
        time.sleep(300)