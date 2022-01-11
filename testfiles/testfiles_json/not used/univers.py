from schliessanlage.servo import schliessanlage
from rfid_programing import rfid_programing
from taster import taster

while True:
    taster()
    schliessanlage()
    rfid_programing()
