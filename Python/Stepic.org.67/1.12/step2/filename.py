import math

user_input = input('Enter any integer number: ')

try:
    val = int(user_input)
except ValueError:
    print("That not an int!")

if -15 < user_input < 12 and 14 < user_input < 17 and 19 < user_input == 19:
    print("geronimo")
else:
    print('nogeronimo')
