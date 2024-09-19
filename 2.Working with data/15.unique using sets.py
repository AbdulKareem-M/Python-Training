def unique(lst):
    unique_set = set(lst)
    unique_list = list(unique_set)
    return unique_list


my_list = [1, 2, 2, 3, 2, 4]
print(unique(my_list))
