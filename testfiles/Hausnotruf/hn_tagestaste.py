import RPi.GPIO as GPIO
from datetime import datetime, timedelta
import time
import hn_taster as alarm

GPIO.setmode(GPIO.BCM)
GPIO.setup(XXX, GPIO.IN) ###Button GPIO pin setzen

#Aktuelle Zeit
x = datetime.now()
t = 46800

def countdown(t):
    while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
        alarm.alarm

