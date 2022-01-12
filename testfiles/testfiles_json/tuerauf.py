import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

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

GPIO.setup(35, GPIO.OUT)  # blaues kabel
GPIO.setup(31, GPIO.OUT)  # gelbes kabel
GPIO.setup(33, GPIO.OUT)  # pinkes kabel
GPIO.setup(29, GPIO.OUT)  # oranges kabel
GPIO.setup(8, GPIO.IN)
GPIO.setup(10, GPIO.IN)


def setStep(w1, w2, w3, w4):
    GPIO.output(35, w1)
    GPIO.output(31, w2)
    GPIO.output(33, w3)
    GPIO.output(29, w4)


def backwards(delay, steps):  # Türe öffnen
    while GPIO.input(10) == 0:  # Stoppt bei passieren der Lichtschranke
        for i in range(steps):
            for j in reversed(range(StepCount)):
                setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
                time.sleep(delay / 1000)


if __name__ == "__main__":
    backwards(1, int(20))  # Rückwärts mit delay = 1 und steps = 20
    print("Tür ist geöffnet!")
