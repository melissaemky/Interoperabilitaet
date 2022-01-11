# Import required library
import xml.etree.ElementTree as xml
x = "TestID"
y = "TestZugang"
z = "TestDatum"


def createXML(filename):
    # Start with the root element
    root = xml.Element("groot")
    users = xml.Element("users")
    root.append(users)
    id = xml.SubElement(users, "id")
    id.text = x
    zugang = xml.SubElement(id, "zugang")
    zugang.text = y
    am = xml.SubElement(id, "am")
    am.text = z

    tree = xml.ElementTree(root)
    with open(filename, "wb") as fh:
        tree.write(fh)


if __name__ == "__main__":
    createXML("/home/pi/config_dateien/univers.xml")
