import xlrd
from statistics import stdev


# Reads data from “AlexaReviews.xlsx”
def read_data():
    records = {}
    try:
        wb = xlrd.open_workbook("AlexaReviews.xlsx")
        sheet = wb.sheet_by_index(0)

        for i in range(1, sheet.nrows):
            color = sheet.cell_value(i, 2).lower().strip()
            rating = sheet.cell_value(i, 1)
            if rating:
                records.setdefault(color, []).append(rating)
    except Exception as err:
        print("Exception while reading products data from file")
        print(err)

    return records


class DarrajHW3Q1:
    # # Reads data from “AlexaReviews.xlsx”
    products = read_data()

    # Calculate the average star rating for all Alexa products
    def compute_average_star_rating_all_products(self):
        for color, ratings in self.products.items():
            average = sum(ratings) / len(ratings)
            average = round(average, 1)
            print(f"Average Star Rating for Product {color.title()} = {average}")

    # function for each of the two colors compute the average, minimum, maximum, range, standard deviation
    def compute_each_two_colors(self):
        while self.products:
            color1, color1_ratings = self.products.popitem()
            color2 = None
            color2_ratings = []

            if self.products:
                color2, color2_ratings = self.products.popitem()
            two_colors_ratings = color1_ratings + color2_ratings

            colors_average = round(sum(two_colors_ratings) / len(two_colors_ratings), 1)
            min_rating = min(two_colors_ratings)
            max_rating = max(two_colors_ratings)
            standard_deviation = round(stdev(color2_ratings), 2)

            print(f"\nColors {color1} & {color2} average = {colors_average}")
            print(f"Colors {color1} & {color2} minimum = {min_rating}")
            print(f"Colors {color1} & {color2} maximum = {max_rating}")
            print(f"Colors {color1} & {color2} range = ({min_rating} - {max_rating})")
            print(f"Colors {color1} & {color2} Standard Deviation = {standard_deviation}")


if __name__ == "__main__":
    # make class object

    obj = DarrajHW3Q1()
    # Call Function Calculate the average star rating for all Alexa products
    obj.compute_average_star_rating_all_products()

    # Call function for each of the two colors compute the average, minimum, maximum, range
    # and standard deviation for the star rating
    obj.compute_each_two_colors()
