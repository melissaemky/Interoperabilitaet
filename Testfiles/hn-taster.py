import RPi.GPIO as GPIO
import time
import pywhatkit as whatsapp

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN)


# Endlosschleife
while True:
    if GPIO.input(16) == 0:
        print("!!!Hausnotrum ALARM!!!")
        whatsapp.sendwhatsmsg("+4915783867643","!!!Alarm!!! Oma braucht Hilfe",18,21)
        #Tür geht auf
        time.sleep(300)

        
