def invertdict(input_dict):
    return {value: key for key, value in input_dict.items()}


my_dict = {'a': 1, 'b': 2, 'c': 3}
inverted = invertdict(my_dict)
print(inverted)