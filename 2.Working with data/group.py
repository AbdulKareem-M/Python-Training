def group(lst, size):
    return [lst[i: i + size] for i in range(0, len(lst) - 1, size)]


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = group(my_list, 4)
print(result)
