import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)

if GPIO.input(21) == 0:
    print("Taster nicht gedrückt")
else:
    print("Taster gedrückt")

'''
# Endlosschleife
while True:
    if GPIO.input(21) == 0:
        print("test")
    # Ausschalten
    else:
        # Einschalten
'''
