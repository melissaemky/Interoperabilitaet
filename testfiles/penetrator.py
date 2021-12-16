from time import sleep
import time
import servo

while 1:
    servo.test(3.5)
    sleep(1)
    servo.test(10)
    sleep(1)
