from lxml import etree
from collections import Counter
import pandas
import re

tree = etree.parse("../parsing_xml/test_menu.xml")   # tree is of type ElementTree
root = tree.getroot()                               # root is Element class

def getvalueofnode(node):
    """ return node text or None """
    if node is not None:
        return node.text
    else:
        None

pandas.set_option('display.max_columns', 20)
pandas.set_option('display.max_colwidth', 90)
dfcols = ['name', 'price', 'description', 'calories']
df_xml = pandas.DataFrame(columns = dfcols)

for i in root.iter('calories'):
    print(i.text)

print('+'*20)
dict = {}
for child in root:
    for grandchild in child:
        print(grandchild.tag, grandchild.text)
        dict.update({grandchild.tag:grandchild.text})
        for greatgrandchild in grandchild:
            print(greatgrandchild.tag)
    #print(child.tag)

print(dict)


print('-'*20)

for tag in root.iter():
    path = tree.getpath(tag)
    #path = path.replace('/', ' ')
    #print('blah', tag.tag, tag.text)
    print(path)

    spaces = Counter(path)
    tag_name = path.split()[-1].split('[')[0]
    tag_name = ' ' * (spaces[' '] - 4) + tag_name
    #print(tag_name)

