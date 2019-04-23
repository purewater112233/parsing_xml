from lxml import etree
from collections import Counter
from remove_autosar_tag import replace_line


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
                print("%s - %s - %s " % (i.tag, i.text, i.attrib))

            # check for an empty string and let the user know
            # if not i.text.strip():
            #     print('There is no text for this tag')


if __name__=="__main__":
    file = 'Cluster_Ethernet_FixedRepeatedShortNames_Rev2_20190311.arxml'
    file_output = 'temp.xml'
    a = ArxmlExtraction(file, file_output)
    a.remove_arxml_namespace()
    a.import_arxml()
    a.iterate_recursively('LENGTH', 'all')
    # a.iterate_recursively('DIAG-PDU-TYPE', 'text')
    # a.iterate_recursively('ELEMENTS', 'text')
    # a.iterate_recursively('I-SIGNAL-IN-I-PDU-REF', 'attrib')
    a.iterate_recursively('ELEMENTS', 'text')
    a.iterate_recursively()

