import time
uni = 1
if uni == 1:
    import RPi.GPIO as GPIO
    servoPIN = 12
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(servoPIN, GPIO.OUT)
    GPIO.setwarnings(False)
    p = GPIO.PWM(servoPIN, 50)  # GPIO 12 als PWM mit 50Hz
    p.start(10)  # Initialisierung


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

def test(winkel):
    if uni == 1:
        p.ChangeDutyCycle(winkel)
        time.sleep(2)
    print(winkel)
    #GPIO.cleanup()
    
tuerzu()