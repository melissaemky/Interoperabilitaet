#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

TASTER = 20
AUSGANG = 15

GPIO.setup(TASTER, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(AUSGANG, GPIO.OUT)

while True:
    tasterStatus = GPIO.input(TASTER)
    if ((tasterStatus) == False):
        print("Test")

try:
    id, text = reader.read()
    print(id)
finally:
    GPIO.cleanup()
