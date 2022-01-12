import requests
import json
import time

zustand="false"

def steckdose(state, id):
    response = requests.put('http://192.168.8.215/api/C0CEFA0EB7/lights/'+ str(id) +'/state', data = '{ "on": '+ zustand +' }')
    print(response)

steckdose(zustand,2)