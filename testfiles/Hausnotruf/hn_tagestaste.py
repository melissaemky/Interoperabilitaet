import time
import datetime
import json

with open ("/home/pi/config_dateien/taster.json") as json_file:
    x = json.load(json_file)

lt = len(x['taster'])
for k in range(0, lt):
    zeitpunkt = (x['taster'][k]['zeitpunkt'])
    if (zeitpunkt-)


unixtime_button = time.mktime(zeitpunkt.timetuple())
unixtime_now = time.mktime(datetime.timetuple())c

