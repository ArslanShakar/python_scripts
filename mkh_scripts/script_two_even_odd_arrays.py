class ArrayInput:
    def get_sorted_arrays(self):
        user_input = input("Please enter comma separated array elements: ")
        odd_array = []
        even_array = []

        for number in user_input.split(','):
            number = (number or '').strip()
            if not number:
                continue

            number = int(number)
            if number % 2 == 0:
                even_array.append(number)
            else:
                odd_array.append(number)

        print("Odd Array: {}".format(odd_array))
        print("------------------------------------")
        print("Even Array: {}".format(even_array))


if __name__ == "__main__":
    ArrayInput().get_sorted_arrays()
