import RPi.GPIO as GPIO
from twilio.rest import Client
import time
from datetime import datetime
import hn_tagestaste
import configparser

import sys                                                          #Twilio Anmeldedaten einbinden
sys.path.insert(1,"/home/pi/config_dateien")
from twilio_anmeldung import auth_token, account_sid, FROM, TO

cfg = configparser.ConfigParser()

#Timestamp
x = datetime.now()

#GPIO set
GPIO.setmode(GPIO.BOARD)
GPIO.setup(36, GPIO.IN)
GPIO.setup(26, GPIO.IN)

#hn-tagestaste - countdown restart
if GPIO.input(26) == 0:
    hn_tagestaste.countdown.exit()
    hn_tagestaste.countdown(int(t))

#Alarm + SMS auslösen
def alarm():
    print("!!!Hausnotruf ALARM!!!\n"+"um "+str(x.hour)+":"+str(x.minute)+" Uhr")
    Client(account_sid, auth_token).messages.create(
        body= "\n!!!Hausnotruf ALARM!!!\n"+"am "+str(x.date),
        to= TO,
        from_= FROM)
    time.sleep(10)

# Endlosschleife Button press ruft Alarm-Funktion auf
while True:
    if GPIO.input(36) == 0:
        alarm()
    
