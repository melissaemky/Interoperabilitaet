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

def time_unix(timetoconvert):
    timetoconvert = timetoconvert[0:19]
    t = time.strptime(timetoconvert, "%Y-%m-%dT%H:%M:%S")
    #print(t)
    unix = int(time.mktime(t))
    return unix

'''
now = time.time()
now = int(now)
print(now)
'''

tasterB1 =requests.get('http://192.168.8.215/api/C0CEFA0EB7/sensors/7/')
body1 = json.loads(tasterB1.text)
state1 = (body1["state"]["buttonevent"])
xtime1 = (body1["state"]["lastupdated"])

tasterB2 =requests.get('http://192.168.8.215/api/C0CEFA0EB7/sensors/8/')
body2 = json.loads(tasterB1.text)
state2 = (body2["state"]["buttonevent"])
xtime2 = (body2["state"]["lastupdated"])

with open ("/home/pi/config_dateien/taster.json") as json_file:
    x = json.load(json_file)
    x["taster"][4]["zustand"]= state1
    x["taster"][4]["zeitpunkt"]= time_unix(xtime1)
    x["taster"][5]["zustand"]= state2
    x["taster"][5]["zeitpunkt"]= time_unix(xtime2)
    print(x)


with open("/home/pi/config_dateien/taster.json", 'w') as json_file:
    json.dump(x, json_file, indent=4)