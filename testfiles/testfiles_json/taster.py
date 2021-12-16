'''
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

GPIO.setmode(GPIO.BOARD)
GPIO.setup(38, GPIO.IN)  # Blauer Taster(Speichern)?
GPIO.setup(40, GPIO.IN)  # Grüner Taser(Löschen)?
'''
