import RPi.GPIO as GPIO
from twilio.rest import Client

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN)

account_sid = "ACd0fd71a46caf82f89a833cebaa7cd506"
auth_token = "c2e789b60f967f6bbaf78d0e9fd3f768"
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