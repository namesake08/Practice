
lst = [1, 2, 3, 4, 5, 6]
book = {
    'title': 'The Langoliers',
    'author': 'Stephen King',
    'year_published': 1990
}

string = "Hello World!"

# for i in string:
#     print(i)

iterator = iter(book)
print(next(iterator))
print(next(iterator))
print(next(iterator))
next(iterator)

for i in book:
    print(i)

#данный цикл аналогичен тому что выше
it = iter(book)
while True:
    try:
        i = next(it)
        print(i)
    except StopIteration:
        break