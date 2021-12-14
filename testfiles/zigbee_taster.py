import requests
import json
import time
import datetime

tasterB1 =requests.get('http://192.168.8.215/api/C0CEFA0EB7/sensors/7/')
body = json.loads(tasterB1.text)
state = (body["state"]["buttonevent"])
time = (body["state"]["lastupdated"])
print(state)
print(time)
x = datetime.datetime.now()
print(x)