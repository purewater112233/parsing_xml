import fileinput, sys

# run this to remove the line at the beginning of an arxml file that contains
# the xmlns (xml namespace) information

def replace_line(file_input, file_output, unwanted_string='xmlns'):
    with open(file_input, "r") as input:
        with open(file_output, "w") as output:
            for line in input:
                if unwanted_string not in line:
                    output.write(line)
                else:
                    output.write("<AUTOSAR>\n")


def replace_in_line(file_name, unwanted_string='xmlns'):
    for line in fileinput.input(file_name, inplace=True):
        if unwanted_string in line:
            line = "<AUTOSAR>\n"
        sys.stdout.write(line)


if __name__ == "__main__":
    unwanted_string = "xmlns"

    # import the arxml file and output an edited xml file
    file_name = "Cluster_Ethernet_FixedRepeatedShortNames_Rev2_20190311.arxml"
    file_output = "removed.xml"
    replace_line(file_name, file_output, unwanted_string)

    # import the arxml file to be overwritten
    file_name = "test.arxml"
    replace_in_line(file_name, unwanted_string)
