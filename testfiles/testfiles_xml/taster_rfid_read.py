import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522
from datetime import datetime
import xml.etree.ElementTree as ET
from xml.dom import minidom
#tree = ET.parse('/home/pi/config_dateien/univers.xml')
#root = tree.getroot()

reader = SimpleMFRC522()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(38, GPIO.IN)  # Blauer Taster(Speichern)
GPIO.setup(40, GPIO.IN)  # Grüner Taser(Loeschen)

'''
ET = ET.ElementTree
ET.write("univers.xml")
dictionary = ET.Element("dictionary")
benutzer = ET.SubElement(dictionary, "benutzer")
id = ET.SubElement(benutzer, "id", {"typ": "int"})
zugang = ET.SubElement(id, "zugang", {"typ": "text"})
am = ET.SubElement(id, "am", {"typ": "yyyy-MM-ddTHH:mm:ss.fffK"})

def speichern():
    id, text = reader.read()
    if id == True:
        print("Karte bekannt")
        zugang.set("gestattet", "gestattet")
        am.set("...", "...")
        print(id)
    else:
        print("Karte unbekannt")
        id = ET.SubElement(benutzer, "id", {"typ": "int"})
        #zugang = ET.SubElement(id, "zugang", {"typ":"text"})
        #am = ET.SubElement(id, "am", {"typ":"yyyy-MM-ddTHH:mm:ss.fffK"})
        zugang.set("gestattet", "gestattet")
        am.set("...", "...")
        print(id)
'''

# hier den Pfad des XML-Files eingeben
xml = ET.parse(open("C:\/home/pi/config_dateien/univers.xml", 'r'))
variables = xml.find('users')
for elems in variables.findall('id'):
    id = elems
    for elem in id.findall("Zugang"):
        print elem.tag, elem.text

'''
def updateET(filename):
    # Start with the root element
    tree = ET.ElementTree(file=filename)
    root = tree.getroot()

    for users in root.iter("users"):
        users.__str__ = str(x)

    tree = ET.ElementTree(root)
    with open("newdata.xml", "wb") as fh:
        tree.write(fh)


if __name__ == "__main__":
    updateET("newdata.xml")


def speichern():
    id, text = reader.read()
    XMLDatei = minidom.parse("univers.xml")
    XMLDatei.getElementsByTagName("users")
    if id == True:
        print("Karte bekannt")
        zugang.set("gestattet", "gestattet")
        am.set("...", "...")
        print(id)
    else:
        print("Karte unbekannt")
        id = ET.SubElement(benutzer, "id", {"typ": "int"})
        zugang = ET.SubElement(id, "zugang", {"typ": "text"})
        am = ET.SubElement(id, "am", {"typ": "yyyy-MM-ddTHH:mm:ss.fffK"})
        zugang.set("gestattet", "gestattet")
        am.set("...", "...")
        print(id)
'''

'''
def löschen():
    id, text = reader.read()
    print(cfg.has_section(str(id)))
    if cfg.has_section(str(id)) == True:
        cfgfile = open(
            "/home/pi/config_dateien/benutzer.ini", 'w')
        cfg.set(str(id), 'zugang', 'verweigert')
        x = datetime.now()
        cfg.set(str(id), 'gelöscht am', str(x))
        cfg.write(cfgfile)
        cfgfile.close()
        print(str(id) + " Zugang verweigert")
    else:
        print("Karte noch nie gespeichert!")
'''

'''
while True:
    if GPIO.input(40) == 0:
        time.sleep(1)
        speichern()
    if GPIO.input(38) == 0:
        time.sleep(1)
        löschen()
'''
