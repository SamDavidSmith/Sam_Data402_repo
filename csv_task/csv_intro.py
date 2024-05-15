import csv

import pandas as pd


class csv_reader:
    def __init__(self, csv_link: str = "user_details.csv"):
        self.csv_link = csv_link

    def transform_csv(self, cols):
        try:
            transform_list = pd.read_csv(self.csv_link, usecols=cols)
            return transform_list
        except FileNotFoundError as msg:
            return "This file doesn't exist"


csv1 = csv_reader()
print(csv_reader.transform_csv(csv1, cols=['firstName', 'lastName', 'email']))


def transform_csv(csv):
    try:
        transform_list = pd.read_csv(csv, usecols=['firstName', 'lastName', 'email'])
        return transform_list
    except FileNotFoundError as msg:
        return "This file doesn't exist"

# print(transform_csv("user_details.csv").iloc[1, 1])
# transform csv_list into transform_list
# ['firstName, 'lastName', 'email']
# include tests
# include functions and try/except

# with open("new_use_details", "w") as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerows(transformed_list)
