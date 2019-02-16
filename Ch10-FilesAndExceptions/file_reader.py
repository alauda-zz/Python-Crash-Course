with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# read line by line
with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line)

# making a list of lines
with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())