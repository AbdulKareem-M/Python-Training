def fn_map(function, iterable):
    return [function(item) for item in iterable]


numbers = [1, 2, 3, 4, 5]
squared_numbers = fn_map(lambda x: x ** 2, numbers)
print(squared_numbers)
