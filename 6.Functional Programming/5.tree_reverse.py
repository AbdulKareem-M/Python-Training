def tree_reverse(nested_list):
    if isinstance(nested_list, list):
        return [tree_reverse(item) for item in reversed(nested_list)]
    else:
        return nested_list


nested_list = [1, [2, [3, 4], 5], 6]
reversed_list = tree_reverse(nested_list)
print(reversed_list)
