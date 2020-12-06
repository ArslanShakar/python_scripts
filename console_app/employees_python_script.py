
# List of Employees Dictionaries each dictionary contains employee information name, salary etc
# Dictionaries are used to store data values in key:value pairs.

employees = []

# get employees input from user
no_of_employees = 0
retry_times = 0

while True:
    try:
        if retry_times > 2:
            print("Retries Limit exceeded. Please try again.")
            exit()

        no_of_employees = int(input("What is the number of employees? "))
        print()
        break
    except Exception as err:
        print("Something went wrong. Please enter correct number...")
        retry_times += 1

if not no_of_employees:
    print("No of employees should greater than zero")
    exit()

while no_of_employees > 0:
    name = input("Enter the employee's name: ")
    salary = float(input("Enter the salary: ").strip())
    print()

    if salary > 5000:
        print("Salary should be capped at 5000. Please try again...")
        continue

    emp = {
        'name': name.strip(),
        'salary': salary
    }

    employees.append(emp)
    no_of_employees -= 1

# necessary coins list
coins = [
        200, 100, 50, 20, 10, 5, 2, 1,
        0.5, 0.20, 0.10, 0.05, 0.02, 0.01
    ]


# A function that will calculate the number of tickets
def get_number_of_tickets(emp_salary):
    temp_salary = 0
    tickets = {}

    for coin in coins:
        tickets[coin] = 0
        if temp_salary == emp_salary:
            continue

        while temp_salary != emp_salary:
            if temp_salary + coin > emp_salary:
                break
            temp_salary += coin
            tickets[coin] += 1

    return tickets


# Calculate ticket numbers for each employee and store tickets result in each employee dictionary
for emp in employees:
    emp['tickets'] = get_number_of_tickets(emp['salary'])

# Display employees data
for emp in employees:
    print("{} in total, you will have to go to the bank to get:\n".format(emp['name']))

    # iterate on employees tickets dictionary and display no. of tickets for each coin
    # dict.items(): Returns a list of dict's (key, value) tuple pairs
    for coin, tickets in emp['tickets'].items():
        print("You will need {} ticket(s) of {}".format(tickets, coin))

    # for making empty new line
    print('\n**************************************************\n')
