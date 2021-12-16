import requests
import json
import time

def lesen():
    pir = requests.get('http://192.168.8.215/api/C0CEFA0EB7/sensors/00:50:43:c9:a3:39:4a:82-01-0500/')
    body = json.loads(pir.text)
    state = (body["state"]["presence"])
    zeitpunkt = (body["lastseen"])
    print(state)
    print(zeitpunkt)
    with open ("/home/pi/config_dateien/universe.json") as json_file:
        x = json.load(json_file)
    x["sensoren"][4]["status"] = state
    x["sensoren"][1]["zeitpunkt"] = zeitpunkt
    with open("/home/pi/config_dateien/universe.json", 'w') as json_file:
        json.dump(x, json_file, indent=4)

#lesen()