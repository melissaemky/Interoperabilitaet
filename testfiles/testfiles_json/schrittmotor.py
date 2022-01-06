import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
coil_A_1_pin = 33  # pink (Farbe der Kabel in Anleitung)
coil_A_2_pin = 29  # orange
coil_B_1_pin = 35  # blau
coil_B_2_pin = 31  # gelb
# enable_pin   = 7 # Nur bei bestimmten Motoren benoetigt (+Zeile 24 und 30)

# anpassen, falls andere Sequenz
StepCount = 8
Seq = list(range(0, StepCount))
Seq[0] = [0, 1, 0, 0]
Seq[1] = [0, 1, 0, 1]
Seq[2] = [0, 0, 0, 1]
Seq[3] = [1, 0, 0, 1]
Seq[4] = [1, 0, 0, 0]
Seq[5] = [1, 0, 1, 0]
Seq[6] = [0, 0, 1, 0]
Seq[7] = [0, 1, 1, 0]

#GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

#GPIO.output(enable_pin, 1)


def setStep(w1, w2, w3, w4):
    GPIO.output(coil_A_1_pin, w1)
    GPIO.output(coil_A_2_pin, w2)
    GPIO.output(coil_B_1_pin, w3)
    GPIO.output(coil_B_2_pin, w4)


def forward(delay, steps):
    for i in range(steps):
        for j in range(StepCount):
            setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay)


def backwards(delay, steps):
    for i in range(steps):
        for j in reversed(range(StepCount)):
            setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay)


if __name__ == '__main__':
    while True:
        delay = input(1) #("Zeitverzoegerung (ms)?")
        steps = input(10) #("Wie viele Schritte vorwaerts? ")
        forward(int(delay) / 1000.0, int(steps))
        steps = input(10) #("Wie viele Schritte rueckwaerts? ")
        backwards(int(delay) / 1000.0, int(steps))
