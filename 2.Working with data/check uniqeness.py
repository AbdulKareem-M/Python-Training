def unique(lst, key=None):
    seen = set()
    result = []
    for item in lst:
        val = item if key is None else key(item)
        if val not in seen:
            seen.add(val)
            result.append(item)
    return result


items = ["apple", "banana", "cherry", "apple", "date", "banana"]
my_list = unique(items)
print(my_list)
