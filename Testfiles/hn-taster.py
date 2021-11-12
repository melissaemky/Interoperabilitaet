import RPi.GPIO as GPIO

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
    if GPIO.input(16) == 1:
        print("!!!Hausnotrum ALARM!!!")

        
