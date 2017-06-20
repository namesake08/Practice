"""У каждого объекта в Python есть:
идентификатор, тип, значение"""

"""Тип объекта не может быть изменен после
создания объекта (как и идентификатор)

Узнать тип объекта можно с помощью функции type()"""

x = [1, 2, 3]
type(x) #output is "<class 'list'>"
type(4)	#output is "<class 'int'>"

#here comes a mindblowing example
type(type(x)) # output is "<class 'type'>"