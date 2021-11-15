import requests
import json
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
GPIO.output(23, GPIO.HIGH)
time.sleep(1)
GPIO.output(23, GPIO.LOW)

"""
while raum == 0:
    pir =requests.get('http://192.168.8.215/api/C0CEFA0EB7/sensors/00:50:43:c9:a3:39:4a:82-01-0500/')
    body = json.loads(pir.text)
    state = (body["state"]["presence"])
    if state == 1:
        print("jemand da")
        raum = 1
"""
