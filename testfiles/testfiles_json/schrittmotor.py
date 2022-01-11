import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
coil_A_1_pin = 35  # blaues kabel
coil_A_2_pin = 31  # gelbes kabel
coil_B_1_pin = 33  # pinkes kabel
coil_B_2_pin = 29  # oranges kabel

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

GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)
GPIO.setup(8, GPIO.IN)
GPIO.setup(10, GPIO.IN)


def setStep(w1, w2, w3, w4):
    GPIO.output(coil_A_1_pin, w1)
    GPIO.output(coil_A_2_pin, w2)
    GPIO.output(coil_B_1_pin, w3)
    GPIO.output(coil_B_2_pin, w4)


def forward(delay, steps):  # Türe schließen
    for i in range(steps):
        for j in range(StepCount):
            setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay / 1000)


def backwards(delay, steps):  # Türe öffnen
    while GPIO.input(10) == 0:  # Stoppt bei passieren der Lichtschranke
        print(GPIO.input(10))
        for i in range(steps):
            for j in reversed(range(StepCount)):
                setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
                time.sleep(delay / 1000)


# Zum testen, nicht in Funktion genutzt:
if __name__ == "__main__":
    while True:
        steps = 200  # Wie viele steps?
        forward(1, int(steps))
        time.sleep(5)
        backwards(1, int(steps))
        time.sleep(5)
