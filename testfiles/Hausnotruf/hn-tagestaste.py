from datetime import datetime
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(XXX, GPIO.IN) ###Button GPIO pin setzen

#Aktuelle Zeit
x = datetime.now()

#Letzten Buttondruck abfragen
while True:
    if GPIO.input(XXX) == 0:
        #die letzte Tagestasten-Zeit mit der aktuellen Zeit vergleichen, wenn Stunden Unterschied > 12h = Alarm
        time.sleep(300)