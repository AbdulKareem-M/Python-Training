def custom_enumerate(input_list):
    result = []
    for index, item in enumerate(input_list):
        result.append((index, item))
    return result


my_list = ['a', 'b', 'c', 'd']
print(custom_enumerate(my_list))
