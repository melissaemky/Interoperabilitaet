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

#Alarm + SMS auslösen
def alarm():
    print("!!!Hausnotruf ALARM!!!\n"+"um "+str(x.hour)+":"+str(x.minute)+" Uhr")
    Client(account_sid, auth_token).messages.create(
        body= "\n!!!Hausnotruf ALARM!!!\n"+"um "+str(x.hour)+":"+str(x.minute)+" Uhr",
        to= TO,
        from_= FROM)
    time.sleep(10)

# Endlosschleife Button press ruft Alarm-Funktion auf
alarm()