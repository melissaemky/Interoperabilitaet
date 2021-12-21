import time
import json

now = time.time()
now = int(now)
print(now)

with open ("/home/pi/config_dateien/taster.json") as json_file:
    x = json.load(json_file)
    print(x["taster"][0]["name"])
    x["taster"][0]["zeitpunkt"]=now

with open("/home/pi/config_dateien/taster.json", 'w') as json_file:
    json.dump(x, json_file, indent=4)


