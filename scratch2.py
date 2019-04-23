import xml.etree.ElementTree as ET
import pandas as pd

file_location = '../parsing_xml/test_menu.xml'

tree = ET.parse(file_location)
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)
    if child.tag == 'food':
        for step_child in child:
            print(step_child.tag)

#iterate over the entire tree
print('-'*40)
print("Iterating using a tree iterator")
print('-'*40)

iter_ = tree.getiterator()
for elem in iter_:
    print(elem.tag)

print('-'*40)

