import xml.etree.ElementTree as ET

tree = ET.parse('../parsing_xml/test_menu.xml')
root = tree.getroot()

print(root.tag)

elemList = []

# get a list of XML tags in the file
def get_tags():
    for elem in tree.iter():
        elemList.append(elem.tag)

    print(elemList)
    print(list(set(elemList)))


get_tags()
print(root.tag)
print(root.attrib)




print('---------------')
for child in root:
    print(child.tag, child.attrib)

print(root[0][1].tag, root[0][1].text, root[0][1].attrib)


print('######################')
for elem in tree.iter():
    print(elem.tag, elem.attrib, elem.text)

for elem in tree.iter(tag='food'):
    print(elem.tag, elem.attrib, elem.text)

print('++++++++++++\n')
for elem in tree.iterfind('food[@name="Belgian blah 1"]'):
    print(elem.tag, elem.attrib, elem.text)

print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
for elem in tree.iterfind('../food'):
    print(elem.tag, elem.attrib, elem.text)

print("000000000000000000000000000000")


elemList = []
for elem in tree.iter():
    print(elem.tag, elem.attrib, elem.text)
    #put all the elem.tag in a list
    elemList.append(elem.tag)

print(elemList)

for elem in tree.iterfind("food"):
    print('test')
    print(elem.tag, elem.attrib)


print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")


import xml.etree.ElementTree as ET

tree = ET.parse('../parsing_xml/test_menu.xml')
root = tree.getroot()
print(root)
print(root.getroot())
print('end')

# for tag in root.iter():
#     path = tree.getpath(tag)
#     path = path.replace('/', '    ')
#     spaces = Counter(path)
#     tag_name = path.split()[-1].split('[')[0]
#     tag_name = ' ' * (spaces[' '] - 4) + tag_name
#     print(tag_name)