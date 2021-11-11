import RPi.GPIO as GPIO
import time

servoPIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50)  # GPIO 18 als PWM mit 50Hz
p.start(2.5)  # Initialisierung
try:
    while True:
        p.ChangeDutyCycle(10)
        time.sleep(2)
        p.ChangeDutyCycle(5)
        time.sleep(2)
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
