import RPi.GPIO as GPIO
from twilio.rest import Client
import time
from datetime import datetime
import hn_tagestaste

#Timestamp
x = datetime.now()

#GPIO set
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN)

#hn-tagestaste - countdown restart
if GPIO.input(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27) == 0:
    hn_tagestaste.countdown.exit()
    hn_tagestaste.countdown(int(t))

# Einrichtung SMS
account_sid = "AC3b9a640bf840e9f26596a841e249f686"
auth_token = "434dd84cb2c80899756e26bcfac488e5"
FROM= '+12674592798'
TO= '+4915770217327'

#Alarm + SMS auslösen
def alarm():
    print("!!!Hausnotruf ALARM!!!\n"+str(x))
    Client(account_sid, auth_token).messages.create(
        body= "\n!!!Hausnotruf ALARM!!!\n"+str(x),
        img= '/img/alarm.png', #vielleicht raus nehmen
        to= TO,
        from_= FROM)
    time.sleep(10)

# Endlosschleife Button press ruft Alarm-Funktion auf
while True:
    if GPIO.input(16) == 0:
        alarm()
    
