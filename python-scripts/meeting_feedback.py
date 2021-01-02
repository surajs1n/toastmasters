# How to use it?
#
# Required - Python 3, make sure it installed on your system.
#
# Direction of use:
# 1. Download the CSV report from bit.ly/evote2
#
# 2. Open terminal/command-prompt and type the following command:
#    python3 <this script's path> <input csv file's path>
#    E.g: python3 meeting_feedback.py /Users/suraj.s/Downloads/HSR\ Toastmasters.csv
#
# 3. You will get the output right on the terminal/command-prompt.


import sys
import csv
import os


# Create directory if doesn't exist
def create_path(file_path):
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))


# Get average of a list
def average(list):
    if (len(list) == 0):
        return 0
    return sum(list) / len(list)


# Function to print ratings and remarks of the dictionary.
def print_remarks(ratings, positive_remarks_dict, negative_remarks_dict):
    print(f'*Total number of votes*: {len(ratings)}\n')

    print(f'*Average Meeting Rating*: {average(ratings):.2f}/5\n')

    print(f'*What went well?*\n-----------------')
    for remark, counts in positive_remarks_dict.items():
        print(f'- {remark} x{counts}')

    print(f'\n\n*What could have been improved?*\n-----------------')
    for remark, counts in negative_remarks_dict.items():
        print(f'- {remark} x{counts}')


# Columns with ratings          -> 8,  12, 15
# Columns with positive remarks -> 9,  13, 16
# Columns with negative remarks -> 10, 14, 17
def read_from_csv_file(input_file_path):
    ratings = []
    positive_remarks = []
    negative_remarks = []

    with open(input_file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)

        for line in csv_reader:
            ratings.extend([line[8], line[12], line[15]])
            positive_remarks.extend([line[9], line[13], line[16]])
            negative_remarks.extend([line[10],line[14], line[17]])

    # Filter-out elements
    ratings          = list(map(int, [rating for rating in ratings if rating]))
    positive_remarks = [remark for remark in positive_remarks if len(remark)>3]
    negative_remarks = [remark for remark in negative_remarks if len(remark)>3]

    positive_remarks_dict = dict((remark, positive_remarks.count(remark)) for remark in set(positive_remarks))
    negative_remarks_dict = dict((remark, negative_remarks.count(remark)) for remark in set(negative_remarks))

    # print(f'{positive_remarks_dict}')
    # print(f'{negative_remarks_dict}')
    # print(f'{ratings}')
    # print(f'{positive_remarks}')
    # print(f'{negative_remarks}')
    print_remarks(ratings, positive_remarks_dict, negative_remarks_dict)


if __name__=="__main__":
    input_file_path = sys.argv[1]
    read_from_csv_file(input_file_path)
