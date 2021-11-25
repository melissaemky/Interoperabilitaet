import time                                             #für time.sleep
import hn_taster                                        #hn_taster importieren

t = 46800                                               # 13h in Sekunden

def countdown(t):                                       #13h countdown
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
        hn_taster.alarm()                               #Alarmfunktion aus hn_taster ausführen

