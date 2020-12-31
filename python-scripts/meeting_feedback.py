# How to use it?
#
# Required - Python 3, make sure it installed on your system.
#
# Direction of use:
# 1. Download the CSV report from bit.ly/evote2
# 2. Open terminal/command-prompt and type the following command:
#    python3 <this script's path> <the csv file's path>
#    E.g: python3 meeting_feedback.py /Users/suraj.s/Downloads/HSR\ Toastmasters.csv
# 3. You will get the output right on the terminal/command-prompt.

import sys
import csv
import os


# Create directory if doesn't exist
def create_path(file_path):
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))


def dump_remarks_on_file(positive_remarks, negative_remarks):
    print(f'What went well?\n=================')
    for remark in positive_remarks:
        print(remark)

    print(f'\n\nWhat could have been improved?\n=================')
    for remark in negative_remarks:
        print(remark)


# Columns with positive remarks -> 9,  13, 16
# Columns with negative remarks -> 10, 14, 17
def read_from_csv_file(input_file_path):
    positive_remarks = []
    negative_remarks = []

    with open(input_file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)

        for line in csv_reader:
            positive_remarks.extend([line[9], line[13], line[16]])
            negative_remarks.extend([line[10],line[14], line[17]])

    # Filter-out empty elements.
    positive_remarks = [remark for remark in positive_remarks if len(remark)>3]
    negative_remarks = [remark for remark in negative_remarks if len(remark)>3]

    # Sort the list lexicographically.
    positive_remarks.sort()
    negative_remarks.sort()

    # print(f'{positive_remarks}')
    # print(f'{negative_remarks}')
    dump_remarks_on_file(positive_remarks, negative_remarks)


if __name__=="__main__":
    input_file_path = sys.argv[1]
    read_from_csv_file(input_file_path)
