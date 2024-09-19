def custom_zip(*iterables):
    min_length = min(len(it) for it in iterables)
    return [(tuple(it[i] for it in iterables)) for i in range(min_length)]


list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

zipped = custom_zip(list1, list2)
print(zipped)
