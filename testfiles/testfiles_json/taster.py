import requests
import json
import time
import RPi.GPIO as GPIO


def time_unix(timetoconvert):
    timetoconvert = timetoconvert[0:19]
    t = time.strptime(timetoconvert, "%Y-%m-%dT%H:%M:%S")
    # print(t)
    unix = int(time.mktime(t))
    return unix


def taster():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(38, GPIO.IN)  # Blauer Taster(Löschen)
    GPIO.setup(40, GPIO.IN)  # Grüner Taster(Speichern)
    GPIO.setup(36, GPIO.IN)  # Roter Taster
    GPIO.setup(37, GPIO.IN)  # Gelber Taster

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

    # Roter Taster
    if GPIO.input(36) == 0:
        print("roter taster gedrückt")
        rot = 1
        zustand = x["taster"][0]["zustand"]
        if rot != zustand:
            print("Zustand Rot war vorher null")
            now = time.time()
            now = int(now)
            x["taster"][0]["zeitpunkt"] = now
            x["taster"][0]["zustand"] = str(rot)
            with open("/home/pi/config_dateien/taster.json", 'w') as json_file:
                json.dump(x, json_file, indent=4)
            print("neuer Zustand: Rot = 1 zurückgeschrieben")
    else:
        zeitpunkt = x["taster"][0]["zeitpunkt"]
        now = time.time()
        now = int(now)
        dif = now - zeitpunkt
        if dif <= 7:
            print("Rot: Abgebrochen")
        else:
            rot = 0
            x["taster"][0]["zustand"] = str(rot)
            with open("/home/pi/config_dateien/taster.json", 'w') as json_file:
                json.dump(x, json_file, indent=4)
    # Blauer Taster
    if GPIO.input(38) == 0:
        print("blauer taster gedrückt")
        blau = 1
        zustand = x["taster"][1]["zustand"]
        if blau != zustand:
            print("Zustand Blau war vorher null")
            now = time.time()
            now = int(now)
            x["taster"][1]["zeitpunkt"] = now
            x["taster"][1]["zustand"] = str(blau)
            with open("/home/pi/config_dateien/taster.json", 'w') as json_file:
                json.dump(x, json_file, indent=4)
            print("neuer Zustand: Blau = 1 zurückgeschrieben")
    else:
        zeitpunkt = x["taster"][1]["zeitpunkt"]
        now = time.time()
        now = int(now)
        dif = now - zeitpunkt
        if dif <= 7:
            print("Blau: Abgebrochen")
        else:
            blau = 0
            x["taster"][1]["zustand"] = str(blau)
            with open("/home/pi/config_dateien/taster.json", 'w') as json_file:
                json.dump(x, json_file, indent=4)
    # Gelber Taster
    if GPIO.input(37) == 0:
        print("gelber taster gedrückt")
        gelb = 1
        zustand = x["taster"][2]["zustand"]
        if gelb != zustand:
            print("Zustand Gelb war vorher null")
            now = time.time()
            now = int(now)
            x["taster"][2]["zeitpunkt"] = now
            x["taster"][2]["zustand"] = str(gelb)
            with open("/home/pi/config_dateien/taster.json", 'w') as json_file:
                json.dump(x, json_file, indent=4)
            print("neuer Zustand: Gelb = 1 zurückgeschrieben")
    else:
        zeitpunkt = x["taster"][2]["zeitpunkt"]
        now = time.time()
        now = int(now)
        dif = now - zeitpunkt
        if dif <= 7:
            print("Gelb: Abgebrochen")
        else:
            gelb = 0
            x["taster"][2]["zustand"] = str(gelb)
            with open("/home/pi/config_dateien/taster.json", 'w') as json_file:
                json.dump(x, json_file, indent=4)
    # Grüner Taster
    if GPIO.input(40) == 0:
        print("grüner taster gedrückt")
        gruen = 1
        zustand = x["taster"][3]["zustand"]
        if gruen != zustand:
            print("Zustand Grün war vorher null")
            now = time.time()
            now = int(now)
            x["taster"][3]["zeitpunkt"] = now
            x["taster"][3]["zustand"] = str(gruen)
            with open("/home/pi/config_dateien/taster.json", 'w') as json_file:
                json.dump(x, json_file, indent=4)
            print("neuer Zustand: Grün = 1 zurückgeschrieben")
    else:
        zeitpunkt = x["taster"][3]["zeitpunkt"]
        now = time.time()
        now = int(now)
        dif = now - zeitpunkt
        if dif <= 7:
            print("Grün: Abgebrochen")
        else:
            gruen = 0
            x["taster"][3]["zustand"] = str(gruen)
            with open("/home/pi/config_dateien/taster.json", 'w') as json_file:
                json.dump(x, json_file, indent=4)

    x["taster"][4]["zustand"] = state1[0]
    x["taster"][4]["zeitpunkt"] = time_unix(xtime1)
    x["taster"][5]["zustand"] = state2[0]
    x["taster"][5]["zeitpunkt"] = time_unix(xtime2)

    with open("/home/pi/config_dateien/taster.json", 'w') as json_file:
        json.dump(x, json_file, indent=4)
