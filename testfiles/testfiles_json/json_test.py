import json

# Write json to a file
sensor = {"name": "Bob",
               "languages": ["English", "Fench"],
               "married": True,
               "age": 32
               }

with open('/home/pi/config_dateien/universe.json', 'w') as json_file:
    json.dump(sensor, json_file)