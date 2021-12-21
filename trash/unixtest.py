import time
import json

now = time.time()
print(now)
now = int(now)
print(now)

with open ("/home/pi/config_dateien/taster.json") as json_file:
    x = json.load(json_file)
    x["taster"][0]["zeitpunkt"]=now

with open("test.json", 'w') as json_file:
    json.dump(x, json_file, indent=4)


