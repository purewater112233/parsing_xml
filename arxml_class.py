from lxml import etree
from collections import Counter
from remove_autosar_tag import replace_line
import re


class ArxmlExtraction:
    def __init__(self, file_name, edited_file_name):
        self.file_name = file_name
        self.edited_file_name = edited_file_name

    def import_arxml(self):
        # import the arxml file
        self.tree = etree.parse(self.edited_file_name)  # tree is an ElementTree instance
        self.root = self.tree.getroot()               # root is an Element instance

    def remove_arxml_namespace(self):
        """
        This function removes the arxml namespace tag to make it like an xml file
        """
        replace_line(self.file_name, self.edited_file_name, 'xmlns')

    def iterate_recursively(self, str_value=None, tag_text_attrib='all'):
        """
        This function returns all the text values for a given tag name
        :param str_value: string to search for
        :param tag_text_attrib: string <'tag', 'text', 'attrib', 'all'>
        :return: values depending on tag_text_attrib
        """

        for i in self.root.iter(str_value):
            if tag_text_attrib == 'tag':
                print(i.tag)
            elif tag_text_attrib == 'text':
                print(i.text)
            elif tag_text_attrib == 'attrib':
                print(i.attrib)
            elif tag_text_attrib == 'all':
                print("%s - %s - %s" % (i.tag, i.text, i.attrib))

            # check for an empty string and let the user know
            # if not i.text.strip():
            #     print('There is no text for this tag')

    def iterate_with_iterparse(self, str_value):
        """
        :param file_name: file to be parsed
        :param str_value: string to search for
        :return:
        """
        for event, elem in etree.iterparse(self.edited_file_name, events=("start", "end")):
            if elem.tag == str_value and event == "end":
                print(elem.text)
                elem.clear()

    def get_xml_tags_tree(self, write_to_file=True):
        """
        :param write_to_file: boolean
        :return:
        """
        if write_to_file:
            f = open("arxml_tag_export.txt", "w")

        # print the arxml tags in a tree format
        for tag in self.root.iter():
            path = self.tree.getpath(tag)
            path = path.replace('/', '    ')
            spaces = Counter(path)
            tag_name = path.split()[-1].split('[')[0]
            #use this split if you want to keep the index for similar tags
            #tag_name = path.split()[-1]
            tag_name = ' ' * (spaces[' '] - 4) + tag_name
            print(tag_name)
            if write_to_file:
                f.write(tag_name + '\n')

        if write_to_file:
            f.close()

    def get_xml_tags_path(self, write_to_file=True, with_brackets=False):
        if write_to_file:
            if with_brackets:
                f = open('arxml_tag_path_export.txt', 'w')
            if not with_brackets:
                f = open('arxml_tag_path_export_no_brackets.txt', 'w')

        # this is the pattern to remove the bracket and number within the bracket
        pattern = r'\[.*?\]'

        for i in self.root.iter():
            path = self.tree.getpath(i)
            if not with_brackets:
                path = re.sub(pattern, '', path)
            print(path)
            if write_to_file:
                f.write(path + '\n')

        if write_to_file:
            f.close()


if __name__=="__main__":
    file = 'Cluster_Ethernet_FixedRepeatedShortNames_Rev2_20190311.arxml'
    file_output = 'temp.xml'
    a = ArxmlExtraction(file, file_output)
    a.remove_arxml_namespace()
    a.import_arxml()
    #a.iterate_recursively('I-SIGNAL-TRIGGERING-REF', 'all')
    #a.iterate_recursively('DIAG-PDU-TYPE', 'attrib')
    # a.iterate_recursively('ELEMENTS', 'text')
    #a.iterate_recursively('I-SIGNAL-PORT', 'all')
    #a.iterate_recursively('SHORT-NAME', 'text')
    #a.iterate_recursively(tag_text_attrib='all')
    #a.get_xml_tags_tree(write_to_file=1)
    #a.iterate_with_iterparse("SHORT-LABEL")
    #a.get_xml_tags_path(write_to_file=1)
    a.get_xml_tags_path(with_brackets=0)
