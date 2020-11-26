date = input("Enter date in the format mm/dd/yyyy: ")
date = date.strip()

if not date or date.count('/') < 2:
    error_message = "Enough characters are not entered\n\n" \
              "Third and 6th character of the strings should have been /\n" \
              "Invalid Date Format"
    print(error_message)
    exit()  # Comment: Terminate the program

for char in date:
    if char.isalpha():
        print("Only digits are allowed for mm, dd and yyyy\nInvalid Date Format")
        exit()  # Terminate the program


if len(date) < 10:
    print("Enough characters are not entered.\nInvalid Date Format")
    exit()

date = date.replace("/", ' ')
print(date)
