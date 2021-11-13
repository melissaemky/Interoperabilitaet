import RPi.GPIO as GPIO
import time
from twilio.rest import Client

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN)

ACCOUNT_SID = 'AC3b9a640bf840e9f26596a841e249f686'
AUTH_TOKEN = 'fdf9ae04ae3555c0dbd08aed5e1eec31'
FROM = 'whatsapp:+14155238886'
To = 'whatsapp:+4915770217327'
whatsapp= f'!!!Hausnotrum ALARM!!!'

# Endlosschleife
while True:
    if GPIO.input(16) == 0:
        print("!!!Hausnotrum ALARM!!!")
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        client.message.create(body=whatsapp, from_=FROM, to=To)
        time.sleep(300)