from time import sleep
import servo

while 1:
    servo.test(3.5)
    sleep(5)
    servo(10)
    sleep(5)