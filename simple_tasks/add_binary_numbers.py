def add_binary_numbers(first_num, second_num):
    result = ''
    carry = 0

    for n1, n2 in zip(reversed(first_num), reversed(second_num)):
        n1 = int(n1)
        n2 = int(n2)

        if n1 > 1 or n2 > 1:
            print("Invalid Input. Binary Number should be 0 or 1")
            return

        add = n1 + n2 + carry
        if add == 2:
            carry = 1
            result = '0' + result

        if add == 1:
            result = '1' + result

        if add == 0:
            result = '0' + result

    print("The sum of {} and {} = {}".format(first_num, second_num, result))


first_num = input("Enter the first number: ")
second_num = input("Enter the second number: ")
add_binary_numbers(first_num, second_num)
