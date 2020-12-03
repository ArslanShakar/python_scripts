# -*- coding: utf-8 -*-

import pandas
import statistics
from textblob import TextBlob


# global function for reading data/rows from excel file using Pandas Library
def get_excel_rows():
    try:
        file_name = 'rest.xlsx'
        read_cols = ['stars', 'review_text']
        data_frame = pandas.read_excel(file_name, usecols=read_cols, dtype={'stars': float})
        return data_frame.to_dict(orient='record')
    except FileNotFoundError as err:
        print("Please provide correct file path: {}".format(err))


class DARRAJEC2Q1:
    records = get_excel_rows()
    stars_dataset = []
    polarities_dataset = []

    # class constructor
    def __init__(self):
        # calculating polarity for each user review_text and make data sets
        for row in self.records:
            polarity = self.calculate_polarity(row['review_text'])
            polarity = round(polarity, 2)
            self.polarities_dataset.append(polarity)
            self.stars_dataset.append(row['stars'])

    def calculate_polarity(self, user_review_text):
        # for calculating review polarity using TextBlob Statistic Library
        return TextBlob(user_review_text or '').polarity

    def calculate_standard_deviation(self, data_set):
        return statistics.stdev(data_set)

    def get_min_stars_rating(self):
        # return min(self.stars_dataset)
        # OR

        min_stars = 6
        for row in self.records:
            # checking data type should be integer or float
            if not isinstance(row['stars'], (int, float)):
                continue

            if row['stars'] < min_stars:
                min_stars = row['stars']

        return min_stars

    def get_max_stars_rating(self):
        # return max(self.stars_dataset)
        # OR

        max_stars = 0
        for row in self.records:
            # checking stars column value data_type should be integer or float
            if not isinstance(row['stars'], (int, float)):
                continue

            if row['stars'] > max_stars:
                max_stars = row['stars']

        return max_stars

    def get_stars_average(self):
        # avg = sum(self.stars_dataset) / len(self.stars_dataset)
        # OR

        avg = 0
        values_count = 0

        for row in self.records:
            # checking data type should be integer or float
            if not isinstance(row['stars'], (int, float)):
                continue
            avg += row['stars']
            values_count += 1

        avg = avg / values_count
        return round(avg, 2)

    def get_stars_range(self):
        return f'({self.get_min_stars_rating()} to {self.get_max_stars_rating()})'

    def get_min_polarity(self):
        return min(self.polarities_dataset)

    def get_max_polarity(self):
        return max(self.polarities_dataset)

    def get_polarity_range(self):
        return f'({self.get_min_polarity()} to {self.get_max_polarity()})'

    def get_polarity_average(self):
        return round(sum(self.stars_dataset) / len(self.stars_dataset), 2)

    def get_stars_standard_deviation(self):
        return self.calculate_standard_deviation(self.stars_dataset)

    def get_polarities_standard_deviation(self):
        return self.calculate_standard_deviation(self.polarities_dataset)

    def display_results(self):
        # Stars analysis results
        print(f"Minimum Stars = {self.get_min_stars_rating()}")
        print(f"Maximum Stars = {self.get_max_stars_rating()}")
        print(f"Average Rating = {self.get_stars_average()}")
        print(f"Stars Range = {self.get_stars_range()}")

        # Polarities analysis results
        print(f"\nMinimum Polarity = {self.get_max_polarity()}")
        print(f"Maximum Polarity = {self.get_max_polarity()}")
        print(f"Average Polarity = {self.get_polarity_average()}")
        print(f"Polarity Range = {self.get_polarity_range()}")

        # Standard Deviation Results for both Stars and Polarities DataSets
        print(f"\nStars Standard Deviation = {self.get_stars_standard_deviation()}")
        print(f"Polarities Standard Deviation = {self.get_polarities_standard_deviation()}")


# main
if __name__ == "__main__":
    # create class object
    darraj_object = DARRAJEC2Q1()

    # call function using class object for displaying results
    darraj_object.display_results()

# The END
