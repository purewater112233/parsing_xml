# helper functions

def check_for_leading_characters(my_string):
    """
    :param my_string: <str>
    :return: my_string: <str> with leading non-alphanumeric numbers removed
    """
    store_index = -1
    for index, letter in enumerate(my_string):
        if not letter.isalpha():
            store_index = index
        else:
            break

    return my_string[(store_index + 1):]

def check_xml_xpath(my_string, file_name):
    """
    This function checks that the XPath is valid
    :param my_string: <str>
    :param file_name: <str>
    :return: flag: <boolean.
    """
    with open(file_name, 'r') as input:
        for line in input:
            if my_string in line:
                flag = True
                break
            else:
                flag = False

    if not flag:
        print('Invalid XML XPath')

    return flag

if __name__=="__main__":
    print(check_for_leading_characters('6hello'))
    print(check_for_leading_characters('hello'))
    print(check_for_leading_characters('.hello'))
    print(check_for_leading_characters('./hello'))
    print(check_for_leading_characters('.//hello'))
    print(check_for_leading_characters('.///hello'))
    print(check_for_leading_characters('.////hello-how-are-you'))
    print(check_for_leading_characters('.////hello-how/are-you'))

    string = 'I-PDU-PORT-REFS/I-PDU-PORT-REF'
    check_xml_xpath(string, 'arxml_tag_path_export_no_brackets.txt')
