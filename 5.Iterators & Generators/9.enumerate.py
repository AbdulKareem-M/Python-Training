def my_enumerate(iterable, start=0):
    index = start
    for item in iterable:
        yield index, item
        index += 1


fruits = ['apple', 'banana', 'cherry']
for index, value in my_enumerate(fruits):
    print(index, value)
