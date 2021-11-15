import RPi.GPIO as GPIO
from twilio.rest import Client

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN)

account_sid = "AC3b9a640bf840e9f26596a841e249f686"
auth_token = "88a999d85cca042e7d31c06a6e7356ad"
FROM= '+12674592798'
TO= '+4915770217327'

# Endlosschleife
while True:
    if GPIO.input(16) == 0:
        print("!!!Hausnotrum ALARM!!!")
        Client(account_sid, auth_token).messages.create(
            body= "!!!Hausnotrum ALARM!!!",
            to= TO,
            from_= FROM)
        time.sleep(300)