Taster = 16
GPIO.setup(TASTER, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

tasterStatus = GPIO.input(TASTER)
if ((tasterStatus) == True):
    print ("Alarm")