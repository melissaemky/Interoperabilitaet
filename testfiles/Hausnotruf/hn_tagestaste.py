"""
import time                                             #für time.sleep
import hn_taster

t = 46800                                               # 13h in Sekunden

def countdown(t):                                       #13h countdown
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer)
        time.sleep(1)
        t -= 1
        hn_taster.alarm()                               #Alarmfunktion aus hn_taster ausführen

"""
with open ("/home/pi/config_dateien/taster.json") as json_file:
    x = json.load(json_file)

lt = len(x['taster'])
for k in range(0, lt):
    zeitpunkt = (x['taster'][k]['zeitpunkt'])
    if (zeitpunkt-)