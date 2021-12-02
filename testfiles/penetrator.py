from time import sleep
import servo
import time

while 1:
    servo.test(3.5)
    sleep(5)
    servo.test(10)
    sleep(5)