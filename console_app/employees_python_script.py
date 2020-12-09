
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
        break
    except Exception as err:
        print("Something went wrong. Please enter correct number...")
        retry_times += 1

if not no_of_employees or no_of_employees > 10:
    print("No of employees should be 1 to 10")
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


def display_message(tickets, coin):
    message = ''
    if coin > 10:
        message = "It will take {} ticket(s) of {}".format(tickets, coin)
    elif 1 <= coin < 10:
        message = "You will need {} coins(s) of {} euro".format(tickets, coin)
    elif coin < 1:
        message = "It will take {} pieces(s) of {} cent".format(tickets, coin)

    if message:
        print(message)


# Calculate ticket numbers for each employee and store tickets result in each employee dictionary
for emp in employees:
    emp['tickets'] = get_number_of_tickets(emp['salary'])

bank_notes = {}
# Display employees data
for emp in employees:
    print("{}'s Salary".format(emp['name']))

    # iterate on employees tickets dictionary and display no. of tickets for each coin
    # dict.items(): Returns a list of dict's (key, value) tuple pairs
    for coin, tickets in emp['tickets'].items():
        bank_notes.setdefault(coin, 0)
        bank_notes[coin] += tickets
        display_message(tickets, coin)

    # for making empty new line
    print('\n**************************************')

# for making empty new line for total bank notes
print('**************************************************')
print('Mr. Debrikedbrok in total, you will have to go to the bank to get:\n')
for coin, ticket_count in bank_notes.items():
    display_message(ticket_count, coin)
