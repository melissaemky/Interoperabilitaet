#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

GPIO.setup(21, GPIO.IN)
GPIO.input(21)

'''try:
    id, text = reader.read()
    print(id)
finally:
    GPIO.cleanup()
