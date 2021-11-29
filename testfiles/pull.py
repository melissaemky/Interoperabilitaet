#!/usr/bin/env python3
import os
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(26, GPIO.IN)  # Grüner Taster(Speichern)

while True:
    if GPIO.input(26) == 0:
        os.system("git pull")

        test