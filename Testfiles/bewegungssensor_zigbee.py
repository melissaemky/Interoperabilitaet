import requests
import json
import time
#from gtts import gTTS
from pygame import mixer
raum = 0
language = 'de'
#tts = gTTS(text="Hallo Alex",
#lang = language, slow = False)
#tts.save("Testfiles\tts.mp3")
mixer.init()
mixer.music.load("Testfiles/test.mp3")
mixer.music.play
"""
while raum == 0:
    pir =requests.get('http://192.168.8.215/api/C0CEFA0EB7/sensors/00:50:43:c9:a3:39:4a:82-01-0500/')
    body = json.loads(pir.text)
    state = (body["state"]["presence"])
    if state == 1:
        print("jemand da")
        raum = 1
"""
