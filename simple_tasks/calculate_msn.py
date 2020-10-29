
binary_value = input("Enter Binary Number: ").strip()

choice = input("Is it two complements ? ( yes / no ): ")
msb = 0

for digit in binary_value:
    if digit not in ['0', '1']:
        print("Invalid Binary value. Binary number should 0 or 1")
        exit()

for d in binary_value.lstrip('0'):
    msb = msb * 2 or 1

if choice.lower() == "yes":
    print("Value on MSB is: {}".format(msb))
else:
    print("Value on MSB is: -{}".format(msb))
