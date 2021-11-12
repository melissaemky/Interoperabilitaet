#!/usr/bin/env python

import RPi.GPIO as GPIO
#from mfrc522 import SimpleMFRC522


#reader = SimpleMFRC522()

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.IN)

for i in range(5):
    GPIO.output(23, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(23, GPIO.LOW)
    time.sleep(0.5)

# Endlosschleife
while True:
    if GPIO.input(24) == 0:
        # Ausschalten
        GPIO.output(23, GPIO.LOW)
    else:
        # Einschalten
        GPIO.output(23, GPIO.HIGH)

'''try:
    id, text = reader.read()
    print(id)
finally:
    GPIO.cleanup()
'''
