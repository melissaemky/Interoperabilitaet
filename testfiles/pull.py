#!/usr/bin/env python3
import os
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(26, GPIO.IN)

while True:
    if GPIO.input(26) == 0:
        os.system("git pull")
<<<<<<< HEAD

        test
=======
>>>>>>> e6fb9c0250d26c5b78f04f2540258da5cbe10762
