import io
import pandas as pd
import xml.etree.ElementTree as ET

file_location = '../parsing_xml/sean_edited_arxml.arxml'

tree = ET.parse(file_location)
root = tree.getroot()

print( root.attrib)

for elem in root:
    print(elem.tag, elem.attrib, elem.text)
print("----------------------------")

for elem in tree.iter():
    print(elem.tag, elem.attrib)
