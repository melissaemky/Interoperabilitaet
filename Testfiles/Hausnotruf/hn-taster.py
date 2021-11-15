import RPi.GPIO as GPIO
import time
import twilio
from  twilio.rest import client

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN)

ACCOUNT_SID = 'AC3b9a640bf840e9f26596a841e249f686'
AUTH_TOKEN = 'fdf9ae04ae3555c0dbd08aed5e1eec31'
FROM = 'whatsapp:+14155238886'
TO = 'whatsapp:+4915770217327'

# Endlosschleife
while True:
    if GPIO.input(16) == 0:
        print("!!!Hausnotrum ALARM!!!")
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        client.message.create(body='!!!Hausnotrum ALARM!!!', from_=FROM, to=TO)
        time.sleep(300)