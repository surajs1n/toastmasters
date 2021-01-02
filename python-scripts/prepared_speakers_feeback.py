



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
def print_remarks(speaker_name, ratings, positive_remarks, negative_remarks):
    print(f'*{speaker_name}*\n-----------------')

    print(f'*Average Meeting Rating*: {average(ratings):.2f}\n')

    print(f'*What went well?*\n-----------------')
    for remark, counts in positive_remarks:
        print(f'- {remark}')

    print(f'\n\n*What could have been improved?*\n-----------------')
    for remark, counts in negative_remarks:
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

    with open(input_file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)

        for line in csv_reader:
            if (number_of_speakers == 0):
                continue

            if (number_of_speakers <= 1):
                first_ratings.extend([line[2]])
                first_positive_remarks.extend([line[3]])
                first_negative_remarks.extend([line[4]])

                # Filter-out elements
                first_ratings          = list(map(int, [rating for rating in first_ratings if rating]))
                first_positive_remarks = [remark for remark in first_positive_remarks if len(remark)>3]
                first_negative_remarks = [remark for remark in first_negative_remarks if len(remark)>3]

                print_remarks("Speaker 1", first_ratings,  first_positive_remarks,  first_negative_remarks)

            if (number_of_speakers <= 2):
                second_ratings.extend([line[5]])
                second_positive_remarks.extend([line[6]])
                second_negative_remarks.extend([line[7]])

                second_ratings          = list(map(int, [rating for rating in second_ratings if rating]))
                second_positive_remarks = [remark for remark in second_positive_remarks if len(remark)>3]
                second_negative_remarks = [remark for remark in second_negative_remarks if len(remark)>3]

                print_remarks("Speaker 2", second_ratings, second_positive_remarks, second_negative_remarks)

            if (number_of_speakers <= 3):
                third_ratings.extend([line[8]])
                third_positive_remarks.extend([line[9]])
                third_negative_remarks.extend([line[10]])

                third_ratings          = list(map(int, [rating for rating in third_ratings if rating]))
                third_positive_remarks = [remark for remark in third_positive_remarks if len(remark)>3]
                third_negative_remarks = [remark for remark in third_negative_remarks if len(remark)>3]

                print_remarks("Speaker 3", third_ratings,  third_positive_remarks,  third_negative_remarks)

            if (number_of_speakers <= 4):
                fourth_ratings.extend([line[11]])
                fourth_positive_remarks.extend([line[12]])
                fourth_negative_remarks.extend([line[13]])

                fourth_ratings          = list(map(int, [rating for rating in fourth_ratings if rating]))
                fourth_positive_remarks = [remark for remark in fourth_positive_remarks if len(remark)>3]
                fourth_negative_remarks = [remark for remark in fourth_negative_remarks if len(remark)>3]

                print_remarks("Speaker 4", fourth_ratings, fourth_positive_remarks, fourth_negative_remarks)


if __name__=="__main__":
    input_file_path = sys.argv[1]
    number_of_speakers = sys.argv[2]
    read_from_csv_file(input_file_path, number_of_speakers)