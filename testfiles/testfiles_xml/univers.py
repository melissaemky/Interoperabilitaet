# Import required library
import xml.etree.ElementTree as xml


def createXML(filename):
    # Start with the root element
    root = xml.Element("groot")
    users = xml.Element("users")
    root.append(users)
    id = xml.SubElement(users, "id")
    id.text = "ID"
    zugang = xml.SubElement(id, "zugang")
    zugang.text = "JA/NEIN"
    am = xml.SubElement(id, "am")
    am.text = "Datum"

    tree = xml.ElementTree(root)
    with open(filename, "wb") as fh:
        tree.write(fh)


if __name__ == "__main__":
    createXML("/home/pi/config_dateien/univers.xml")
