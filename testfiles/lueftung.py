import time
import RPi.GPIO as GPIO
from humidity import read(self) as Sensor
servoPIN = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)
p = GPIO.PWM(servoPIN, 50)          # GPIO 12 als PWM mit 50Hz
p.start(10)                         # Initialisierung

""""
def luefteran():
    p.ChangeDutyCycle(10)
    print("Lüfter ist aus!")
    time.sleep(2)


def luefteraus():
    p.ChangeDutyCycle(5)
    print("Lüfter ist an!")
    time.sleep(2)

if (luftquaität < richtwert):
    luefteran()
    time.sleep(30)
else: luefteraus()
"""
print (Sensor())