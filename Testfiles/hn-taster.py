import RPi.GPIO as GPIO
import time
import pywhatkit as kit

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN)


# Endlosschleife
while True:
    if GPIO.input(16) == 0:
        print("!!!Hausnotrum ALARM!!!")
        kit.sendwhatmsg_instantly(f"+4915783867643","!!!Hausnotrum ALARM!!!",14,3)
        #kit.sendwhats_image(phone_no="+4915783867643",img_path="img/Oma.jpg",caption="!!!Alarm!!! Oma braucht Hilfe")
        #Tür geht auf
        time.sleep(300)

        
