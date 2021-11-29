# Import required library
import xml.etree.ElementTree as xml


def createXML(filename):
    # Start with the root element
    root = xml.Element("users")
    children1 = xml.Element("user")
    root.append(children1)

    userId1 = xml.SubElement(children1, "Id")
    userId1.text = "hello"

    userName1 = xml.SubElement(children1, "Name")
    userName1.text = "Rajesh"

    tree = xml.ElementTree(root)
    with open(filename, "wb") as fh:
        tree.write(fh)


if __name__ == "__main__":
    createXML("testXML.xml")
