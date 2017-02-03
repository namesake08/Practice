#print -- это функция
print ("Hello world!")

test = 10

print("Мне " + str(test) + " лет")

stroka = '''Это многострочная строка. Это её первая строка.
Это её вторая строка.
"What's your name?", - спросил я.
Он ответил: "Bond, James Bond."
'''

print(stroka)

a = input('Введите первое число : ')
b = input("Введите второе число : ")

print(int(a) + int(b))

name = input("Введите Ваше Имя : ")
count = input('Сколько раз умножить? : ')

print(name * int(count))

x = [10, 2, 5, 7]
x.sort()
print(x)