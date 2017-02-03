# Write a program that accept the sequence of numbers 
# and outputs their sum

n = int(input('Введите число от 1 до 100: '))
b = 0
i = 0

if n >= 1 and n <= 100:
    while i != n:
        a = int(input('Enter a number: '))
        b += a
        i += 1
else: 
    print ('Неверное число')

print(b)
