import time
uni = 0
if uni == 1:
    import RPi.GPIO as GPIO
    servoPIN = 18
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN, GPIO.OUT)
    p = GPIO.PWM(servoPIN, 50)  # GPIO 18 als PWM mit 50Hz
    p.start(2.5)  # Initialisierung


def tuerzu():
    if uni == 1:
        p.ChangeDutyCycle(10)
    print("Tür ist geschlossen!")
    time.sleep(2)


def tuerauf():
    if uni == 1:
        p.ChangeDutyCycle(5)
    print("Tür ist geöffnet!")
    time.sleep(2)


tuerzu()
