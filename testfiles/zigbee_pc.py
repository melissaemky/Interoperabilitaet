import requests
import json
import time

'''
pir =requests.get('http://192.168.8.215/api/C0CEFA0EB7/sensors/00:50:43:c9:a3:39:4a:82-01-0500/')
body = json.loads(pir.text)
state = (body["state"]["presence"])
print(state)
'''

def steckdose():
    response = requests.put('http://192.168.8.215/api/C0CEFA0EB7/lights/2/state',data = '{ "on": false }')
    print(response)

steckdose()