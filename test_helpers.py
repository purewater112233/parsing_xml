import pytest
from helpers import check_for_leading_characters
from helpers import check_xml_each_tag_name
from helpers import check_xml_xpath

@pytest.mark.parametrize('my_string,expected', [('6hello', 'hello'),
                                                ('hello', 'hello'),
                                                ('.hello', 'hello'),
                                                ('./hello', 'hello'),
                                                ('.//hello', 'hello'),
                                                ('.///hello', 'hello'),
                                                ('.////hello-how-are-you', 'hello-how-are-you'),
                                                ('.////hello-how/are-you', 'hello-how/are-you')])
def test_check_for_leading_characters(my_string, expected):
    assert check_for_leading_characters(my_string) == expected

@pytest.mark.parametrize('my_string,expected',
                         [('I-PDU-PORT-REFS/I-PDU-PORT-REF', True),
                          ('aI-PDU-PORT-REFS/I-PDU-PORT-REF', False),
                          ('DU-PORT-REFS/I-PDU-PORT-REF', False),
                          ('I-PDU-PORT-REF', True)])
def test_check_xml_xpath(my_string, expected):
    file = 'arxml_tag_path_export_no_brackets.txt'
    assert check_xml_xpath(my_string, file) == expected
