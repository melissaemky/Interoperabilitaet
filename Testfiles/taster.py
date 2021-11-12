import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)

# Endlosschleife
while True:
    if GPIO.input(21) == 0:
        print("test")
    # Ausschalten
    else:
        # Einschalten
