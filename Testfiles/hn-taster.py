import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN)
"""
if GPIO.input(16) == 0:
    print("Taster nicht gedrückt")
else:
    print("Taster gedrückt")
"""

# Endlosschleife
while True:
    if GPIO.input(16) == 0:
        print("!!!Hausnotrum ALARM!!!")
        time.sleep(1)

        
