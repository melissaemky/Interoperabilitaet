import time
import RPi.GPIO as GPIO

def tuerini():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setwarnings(False)

def tuerzu():
    p = GPIO.PWM(12, 50)  # GPIO 12 als PWM mit 50Hz
    p.ChangeDutyCycle(10)
    print("Tür ist geschlossen!")
    time.sleep(2)
    GPIO.cleanup()

def tuerauf():
    p = GPIO.PWM(12, 50)  # GPIO 12 als PWM mit 50Hz
    p.ChangeDutyCycle(3.5)
    print("Tür ist geöffnet!")
    time.sleep(2)
    GPIO.cleanup()


def test(winkel):
    p.ChangeDutyCycle(winkel)
    time.sleep(2)
    print(winkel)

<<<<<<< HEAD
    GPIO.cleanup()
=======
türini()
p = GPIO.PWM(12, 50)  # GPIO 12 als PWM mit 50Hz
p.start(10)  # Initialisierung
time.sleep(2)
GPIO.cleanup()
>>>>>>> abaeb3e3d9f137486ea09b6b32ba85f99f3cc812
