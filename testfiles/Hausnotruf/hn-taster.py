import RPi.GPIO as GPIO
import twilio
import twilio.rest

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN)

account_sid = "AC3b9a640bf840e9f26596a841e249f686"
auth_token = "fdf9ae04ae3555c0dbd08aed5e1eec31"
FROM= '+14155238886'
TO= '+4915770217327'

# Endlosschleife
while True:
    if GPIO.input(16) == 0:
        print("!!!Hausnotrum ALARM!!!")
        client = twilio.rest.Client(account_sid, auth_token)
        client.messages.create(
            to=TO,
            from_=FROM,
            body="!!!Hausnotrum ALARM!!!")
        time.sleep(300)