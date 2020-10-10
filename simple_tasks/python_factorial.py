print("Use a negative number to terminate input")


def factorial(num):  # function definition
    fact = 1

    for i in range(1, num + 1):  # for loop for finding factorial
        fact = fact * i
    return fact  # return factorial


while True:
    number = int(input("Enter an integer: "))
    if number < 1:
        exit(0)

    fact_result = factorial(number)
    print("{}! is {}".format(number, fact_result))
