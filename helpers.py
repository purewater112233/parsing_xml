# helper functions to parse XML XPath


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
    This function checks the XPath string against the arxml XPath file
    to make sure it is valid
    :param my_string: <str>
    :param file_name: <str>
    :return: flag: <boolean.
    """

    unique_paths_file = 'unique_arxml_tag_paths.txt'
    non_unique_paths_file = file_name

    get_unique_paths(non_unique_paths_file, unique_paths_file)
    file_name = unique_paths_file

    my_string = check_for_leading_characters(my_string)

    with open(file_name, 'r') as input:
        for line in input:
            if check_xml_each_tag_name(my_string, line):
                if my_string in line:
                    flag = True
                break
            else:
                flag = False

    if not flag:
        print('Invalid XML XPath')

    return flag


def check_xml_each_tag_name(my_string, target_string):
    """
    This function checks that a string is a subset of the XPath string
    :param my_string:
    :param target_string:
    :return:
    """
    my_string = my_string.replace('/', ' ')
    my_string = my_string.split()

    target_string = target_string.replace('/', ' ')
    target_string = target_string.split()

    if set(my_string).issubset(set(target_string)):
        return True
    else:
        return False


def get_unique_paths(input_file, output_file):
    """
    This function gets the unique paths from an input file and writes it
    to an output file
    :param input_file: <str>
    :param output_file: <str>
    :return:
    """
    lines_seen = set()

    input = open(input_file, 'r')
    output = open(output_file, 'w')

    for line in input:
        if line not in lines_seen:
            output.write(line)
            lines_seen.add(line)

    output.close()


if __name__=="__main__":
    print(check_for_leading_characters('6hello'))
    print(check_for_leading_characters('hello'))
    print(check_for_leading_characters('.hello'))
    print(check_for_leading_characters('./hello'))
    print(check_for_leading_characters('.//hello'))
    print(check_for_leading_characters('.///hello'))
    print(check_for_leading_characters('.////hello-how-are-you'))
    print(check_for_leading_characters('.////hello-how/are-you'))

    string = 'I-PDU-PORT-REF'
    string2 = 'AR-PACKAGE/I-PDU-PORT-REFS/I-PDU-PORT-REF'
    print(check_xml_xpath(string, 'arxml_tag_path_export_no_brackets.txt'))
    print(check_xml_xpath(string2, 'arxml_tag_path_export_no_brackets.txt'))
