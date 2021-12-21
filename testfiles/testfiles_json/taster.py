'''
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

GPIO.setmode(GPIO.BOARD)
GPIO.setup(38, GPIO.IN)  # Blauer Taster(Speichern)?
GPIO.setup(40, GPIO.IN)  # Grüner Taser(Löschen)?
'''

import time
import json
import requests

now = time.time()
now = int(now)
print(now)

tasterB1 =requests.get('http://192.168.8.215/api/C0CEFA0EB7/sensors/7/')
body = json.loads(tasterB1.text)
state = (body["state"]["buttonevent"])
time = (body["state"]["lastupdated"])
print(state)
print(time)

'''

with open ("/home/pi/config_dateien/taster.json") as json_file:
    x = json.load(json_file)
    print(x["taster"][0]["name"])
    x["taster"][0]["zeitpunkt"]=now

with open("/home/pi/config_dateien/taster.json", 'w') as json_file:
    json.dump(x, json_file, indent=4)

'''