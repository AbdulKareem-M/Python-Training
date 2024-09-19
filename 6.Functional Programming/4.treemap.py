def treemap(func, nested_list):
    if isinstance(nested_list, list):
        return [treemap(func, item) for item in nested_list]
    else:
        return func(nested_list)


nested_list = [1, [2, [3, 4], 5], 6]
result = treemap(lambda x: x * 2, nested_list)
print(result)
