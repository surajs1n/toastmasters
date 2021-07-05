# How to use it?
#
# Required - Python 3, make sure it installed on your system.
#
# Direction of use:
# 1. Download the CSV report from bit.ly/hsrtm-v1
#
# 2. Open terminal/command-prompt and type the following command:
#    python3 <this script's path> <input csv file's path> <number of speakers>
#    E.g: python3 prepared_speakers_feedback.py /Users/suraj.s/Downloads/HSR\ Toastmasters.csv 4
#
# 3. You will get the output right on the terminal/command-prompt.


import sys
import csv
import os
import itertools


# Create directory if doesn't exist
def create_path(file_path):
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))


# Get average of a list
def average(list):
    if (len(list) == 0):
        return 0
    return sum(list) / len(list)


def split_string(array_list):
    returned_list = []
    for str in array_list:
        returned_list.extend(str.split(';'))

    return returned_list


# Function to print ratings and remarks of the dictionary.
def print_remarks(speaker_name, ratings, positive_remarks_dict, negative_remarks_dict):
    print(f'*{speaker_name}*\n-----------------')

    print(f'*Audience votes count*: {len(ratings)}')

    print(f'*Average Rating*: {average(ratings):.2f}/5\n')

    print(f'*What went well?*\n-----------------')
    for remark, counts in positive_remarks_dict.items():
        if counts > 1:
            print(f'- {remark} *x{counts}*')
        else:
            print(f'- {remark}')

    print(f'\n*What could have been improved?*\n-----------------')
    for remark, counts in negative_remarks_dict.items():
        if counts > 1:
            print(f'- {remark} *x{counts}*')
        else:
            print(f'- {remark}')

    print(f'\n\n')


def read_from_csv_file(input_file_path, number_of_speakers):
    first_ratings = []
    first_positive_remarks = []
    first_negative_remarks = []

    second_ratings = []
    second_positive_remarks = []
    second_negative_remarks = []

    third_ratings = []
    third_positive_remarks = []
    third_negative_remarks = []

    fourth_ratings = []
    fourth_positive_remarks = []
    fourth_negative_remarks = []

    guest_names = []
    guest_phonenumber = []
    guest_connect = []


    with open(input_file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)

        for line in csv_reader:
            if (number_of_speakers == 0):
                continue

            if (number_of_speakers >= 1):
                first_ratings.extend([line[2]])
                first_positive_remarks.extend([line[3]])
                first_negative_remarks.extend([line[4]])

                if (number_of_speakers >= 2):
                    second_ratings.extend([line[5]])
                    second_positive_remarks.extend([line[6]])
                    second_negative_remarks.extend([line[7]])

                    if (number_of_speakers >= 3):
                        third_ratings.extend([line[8]])
                        third_positive_remarks.extend([line[9]])
                        third_negative_remarks.extend([line[10]])

                        if (number_of_speakers >= 4):
                            fourth_ratings.extend([line[11]])
                            fourth_positive_remarks.extend([line[12]])
                            fourth_negative_remarks.extend([line[13]])

                            # copy for four people
                            if (line[14] == 'Guest'):
                                guest_names.append(line[15])
                                guest_phonenumber.append(line[16])
                                guest_connect.append(line[17])
                        else:
                            # copy for three people
                            if (line[11] == 'Guest'):
                                guest_names.append(line[12])
                                guest_phonenumber.append(line[13])
                                guest_connect.append(line[14])
                    else:
                        # copy for two people
                        if (line[8] == 'Guest'):
                            guest_names.append(line[9])
                            guest_phonenumber.append(line[10])
                            guest_connect.append(line[11])
                else:
                    # copy for single person
                    if (line[5] == 'Guest'):
                        guest_names.append(line[6])
                        guest_phonenumber.append(line[7])
                        guest_connect.append(line[8])
            else:
                # copy for empty list
                if (line[2] == 'Guest'):
                    guest_names.append(line[3])
                    guest_phonenumber.append(line[4])
                    guest_connect.append(line[5])


         # Filter-out elements
        first_ratings = list(map(int, [rating for rating in first_ratings if rating]))
        first_positive_remarks = [remark for remark in first_positive_remarks if len(remark)>3]
        first_positive_remarks = split_string(first_positive_remarks)
        first_negative_remarks = [remark for remark in first_negative_remarks if len(remark)>3]
        first_negative_remarks = split_string(first_negative_remarks)

        first_positive_remarks_dict = dict(
            (remark, first_positive_remarks.count(remark)) for remark in set(first_positive_remarks))
        first_negative_remarks_dict = dict(
            (remark, first_negative_remarks.count(remark)) for remark in set(first_negative_remarks))
        print_remarks("Speaker 1", first_ratings,  first_positive_remarks_dict,  first_negative_remarks_dict)

        second_ratings = list(map(int, [rating for rating in second_ratings if rating]))
        second_positive_remarks = [remark for remark in second_positive_remarks if len(remark)>3]
        second_positive_remarks = split_string(second_positive_remarks)
        second_negative_remarks = [remark for remark in second_negative_remarks if len(remark)>3]
        second_negative_remarks = split_string(second_negative_remarks)

        second_positive_remarks_dict = dict(
            (remark, second_positive_remarks.count(remark)) for remark in set(second_positive_remarks))
        second_negative_remarks_dict = dict(
            (remark, second_negative_remarks.count(remark)) for remark in set(second_negative_remarks))
        print_remarks("Speaker 2", second_ratings, second_positive_remarks_dict, second_negative_remarks_dict)

        third_ratings = list(map(int, [rating for rating in third_ratings if rating]))
        third_positive_remarks = [remark for remark in third_positive_remarks if len(remark)>3]
        third_positive_remarks = split_string(third_positive_remarks)
        third_negative_remarks = [remark for remark in third_negative_remarks if len(remark)>3]
        third_negative_remarks = split_string(third_negative_remarks)

        third_positive_remarks_dict = dict(
            (remark, third_positive_remarks.count(remark)) for remark in set(third_positive_remarks))
        third_negative_remarks_dict = dict(
            (remark, third_negative_remarks.count(remark)) for remark in set(third_negative_remarks))
        print_remarks("Speaker 3", third_ratings,  third_positive_remarks_dict,  third_negative_remarks_dict)

        fourth_ratings = list(map(int, [rating for rating in fourth_ratings if rating]))
        fourth_positive_remarks = [remark for remark in fourth_positive_remarks if len(remark)>3]
        fourth_positive_remarks = split_string(fourth_positive_remarks)
        fourth_negative_remarks = [remark for remark in fourth_negative_remarks if len(remark)>3]
        fourth_negative_remarks = split_string(fourth_negative_remarks)

        fourth_positive_remarks_dict = dict(
            (remark, fourth_positive_remarks.count(remark)) for remark in set(fourth_positive_remarks))
        fourth_negative_remarks_dict = dict(
            (remark, fourth_negative_remarks.count(remark)) for remark in set(fourth_negative_remarks))
        print_remarks("Speaker 4", fourth_ratings, fourth_positive_remarks_dict, fourth_negative_remarks_dict)

        print(f'*Guest list:*\n-----------------')
        for (name, phone_number, connect) in itertools.zip_longest(guest_names, guest_phonenumber, guest_connect, fillvalue="N/A"):
            print(f'- {name}, {phone_number}, {connect}')


if __name__ == "__main__":
    input_file_path = sys.argv[1]
    number_of_speakers = int(sys.argv[2])
    read_from_csv_file(input_file_path, number_of_speakers)