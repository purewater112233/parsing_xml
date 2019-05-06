import xml.etree.ElementTree as ET


def get_xml_tag_tree(elem, indent = 0):
    print(' ' * indent + elem.tag)
    f.write(' ' * indent + elem.tag + '\n')
    for child in elem.findall('*'):
        get_xml_tag_tree(child, indent + 4)


if __name__ == '__main__':
    tree = ET.parse("temp_arxml.xml")
    root = tree.getroot()  # root is an Element instance
    f = open('arxml_tag_tree_export.txt', 'w')
    get_xml_tag_tree(root)
