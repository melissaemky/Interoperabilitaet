import ntplib
from time import ctime
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(XXX, GPIO.IN) ###Button GPIO pin setzen

###pip install ntplib

#Zeit aus Netz holen
def print_time():
    ntpClient = ntplib.ntpClient()
    response = ntpClient.request('pool.ntp.org')

    print(ctime(response.tx_time))

if __name__ == "__main__":
        print_time()

#Letzten Buttondruck abfragen
while True:
    if GPIO.input(XXX) == 0:
        #die letzte Tagestasten-Zeit mit der aktuellen Zeit vergleichen, wenn Stunden Unterschied > 12h = Alarm
        time.sleep(300)