import RPi.GPIO as GPIO
import time
import pywhatkit as whatsapp

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN)


# Endlosschleife
while True:
    if GPIO.input(16) == 0:
        print("!!!Hausnotrum ALARM!!!")
        whatsapp.sendwhats_image(phone_no="+4915783867643",img_path="img/Oma.jpg",caption="!!!Alarm!!! Oma braucht Hilfe")
        #Tür geht auf
        time.sleep(300)

        
