import xml.etree.ElementTree as ET
xml_tree = ET.parse('/home/pi/config_dateien/univers.xml')
xml_root = xml_tree.getroot()
# Header
print('Tutorial List :')
for movie in xml_root.iter('Tutorial'):
    print(movie.attrib)

'''
for xml_elmt in xml_root:
    for inner_elmt in xml_elmt:
        print(inner_elmt.text)
'''
