import RPi.GPIO as GPIO
from twilio.rest import Client
import time
#import ntplib
#from time import ctime

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN)
# Einrichtung SMS
account_sid = "AC3b9a640bf840e9f26596a841e249f686"
auth_token = "434dd84cb2c80899756e26bcfac488e5"
FROM= '+12674592798'
TO= '+491570217327'

# Zeitstempel
"""def print_time():
    ntpClient = ntplib.ntpClient()
    response = ntpClient.request('pool.ntp.org')

    print(ctime(response.tx_time))

if __name__ == "__main__":
        print_time()"""

# Endlosschleife
while True:
    if GPIO.input(16) == 0:
        print("!!!Hausnotruf ALARM!!!")
        Client(account_sid, auth_token).messages.create(
            body= "!!!Hausnotruf ALARM!!!",
            to= TO,
            from_= FROM)
        time.sleep(10)

