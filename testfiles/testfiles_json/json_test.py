import json

"""
x = {
  "sensoren": [
    {"id": "0", "typ": "temperatur", "messwert": 20},
    {"id": "1", "typ": "luftfeuchte", "messwert": 24.1}
  ]
}

#print(json.dumps(x,))

with open("test.json", 'w') as json_file:
    json.dump(x, json_file, indent=4)

"""
with open ("test.json") as json_file:
    x = json.load(json_file)
    temp = (x['sensoren'][0]["messwert"])
    print(temp)
    x["sensoren"][0]["messwert"]=temp+1

with open("test.json", 'w') as json_file:
    json.dump(x, json_file, indent=4)

