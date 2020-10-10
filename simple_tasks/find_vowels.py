line = input("Type a line of text: ")
line = line.lower()

vowels_count = 0

for char in ['a', 'e', 'i', 'o', 'u']:
    vowels_count += line.count(char)

print("The line contains {} vowels".format(vowels_count))
