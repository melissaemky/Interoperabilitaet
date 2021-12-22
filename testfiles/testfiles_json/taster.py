import requests
import json
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(38, GPIO.IN)  # Blauer Taster(Speichern)?
GPIO.setup(40, GPIO.IN)  # Grüner Taser(Löschen)?


def time_unix(timetoconvert):
    timetoconvert = timetoconvert[0:19]
    t = time.strptime(timetoconvert, "%Y-%m-%dT%H:%M:%S")
    # print(t)
    unix = int(time.mktime(t))
    return unix


while(1):
    with open("/home/pi/config_dateien/taster.json") as json_file:
        x = json.load(json_file)

    tasterB1 = requests.get('http://192.168.8.215/api/C0CEFA0EB7/sensors/7/')
    body1 = json.loads(tasterB1.text)
    state1 = str(body1["state"]["buttonevent"])
    xtime1 = (body1["state"]["lastupdated"])

    tasterB2 = requests.get('http://192.168.8.215/api/C0CEFA0EB7/sensors/8/')
    body2 = json.loads(tasterB2.text)
    state2 = str(body2["state"]["buttonevent"])
    xtime2 = (body2["state"]["lastupdated"])

    if GPIO.input(38) == 0:
        blau = 1
        zustand = x["taster"][1]["zustand"]
        if blau != zustand:
            now = time.time()
            now = int(now)
            x["taster"][1]["zeitpunkt"] = now
            x["taster"][1]["zustand"] = str(blau)
            with open("/home/pi/config_dateien/taster.json", 'w') as json_file:
                json.dump(x, json_file, indent=4)
    else:
        blau = 0
    if GPIO.input(40) == 0:
        gruen = 1
    else:
        gruen = 0

        x["taster"][4]["zustand"] = state1[0]
        x["taster"][4]["zeitpunkt"] = time_unix(xtime1)
        x["taster"][5]["zustand"] = state2[0]
        x["taster"][5]["zeitpunkt"] = time_unix(xtime2)
        x["taster"][1]["zustand"] = str(blau)
        x["taster"][3]["zustand"] = str(gruen)

    with open("/home/pi/config_dateien/taster.json", 'w') as json_file:
        json.dump(x, json_file, indent=4)
