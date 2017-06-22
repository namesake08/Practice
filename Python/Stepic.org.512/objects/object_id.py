"""У каждого объекта в Python есть:
идентификатор, тип, значение"""


"""Получить идентификатор - id()"""
x = [1, 2, 3]
print(id(x)) # output is 140132397244232
print(id([1, 2, 3]))#output is 140132397253384


"""Ccылаются ли две переменные на один объект можно оператором is"""
x = [1, 2, 3]
y = x
y is x			#True
y is [1, 2, 3]	#False

"""Изменяется объект, а не переменная"""
x = [1, 2, 3]
y = x
print(y is x)	#True
x.append(4)
print(x)	# [1, 2, 3, 4]
print(y)	# [1, 2, 3, 4]

s = '123'
t = s
t = t + '4'	#"1234"
print(str(x) + ' ' +s)#[1, 2, 3, 4] 123