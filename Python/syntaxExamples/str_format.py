#!/usr/bin/env python3

age = 25
name = 'Namesake'

print('Возраст {0} -- {1} лет.'.format(name, age))
print('Почему {0} забавляется с этим Python'.format(name))


age = 33
name = "Swaroop"

print("Возраст {} -- {} года.".format(name, age))
print('Почему {} забавляется с этим Python?'.format(name))

# десятичное число (.) с точностью в 3 знака для плавающих:
print('{0:.3}'.format(1/3))

# заполнить подчеркиванием (_) с центровкой текста (^) по ширине 11:
print('{:_^27}'.format('hello'))

# по ключевым словам:
print('{name} написал {book}'.format(name='Swaroop', book="A Byte of Python"))