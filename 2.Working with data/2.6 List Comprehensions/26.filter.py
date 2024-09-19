def custom_filter(function, iterable):
    return [item for item in iterable if function(item)]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = custom_filter(lambda x: x % 2 == 0, numbers)
print(even_numbers)