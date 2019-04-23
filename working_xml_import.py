from lxml import etree
from collections import Counter

file_name = "removed_xmlns.arxml"

# import the arxml file

tree = etree.parse("../parsing_xml/removed_xmlns.arxml")    # tree is an ElementTree instance
root = tree.getroot()                                       # root is an Element instance

print(type(tree))
print(type(root))

f = open("arxml_tag.txt", "w")

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