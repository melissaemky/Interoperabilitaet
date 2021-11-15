import RPi.GPIO as GPIO
from twilio.rest import Client

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN)

account_sid = "AC3b9a640bf840e9f26596a841e249f686"
auth_token = "fdf9ae04ae3555c0dbd08aed5e1eec31"
FROM= '0014155238886'
TO= '004915770217327'

# Endlosschleife
while True:
    if GPIO.input(16) == 0:
        print("!!!Hausnotrum ALARM!!!")
        Client(account_sid, auth_token).messages.create(
            body= "!!!Hausnotrum ALARM!!!",
            to= TO,
            from_= FROM)
        time.sleep(300)