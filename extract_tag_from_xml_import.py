from lxml import etree
from collections import Counter

# make sure to delete the line from that arxml file that starts with <AUTOSAR xmlns="http://autosar.org/schema/r4.0" ...

# import the arxml file

tree = etree.parse("../parsing_xml/sean_edited_arxml.arxml")    # tree is an ElementTree instance
root = tree.getroot()                                           # root is an Element instance

# put all the tags into a text file
f = open("arxml_tag.txt", "a")

# print the arxml tags in a tree format
for tag in root.iter():
    path = tree.getpath(tag)
    path = path.replace('/', '    ')
    spaces = Counter(path)
    tag_name = path.split()[-1].split('[')[0]
    tag_name = ' ' * (spaces[' '] - 4) + tag_name
    print(tag_name)
    f.write(tag_name + '\n')

f.close()
