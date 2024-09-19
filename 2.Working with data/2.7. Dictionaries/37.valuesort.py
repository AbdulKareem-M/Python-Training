def valuesort(d):
    return [d[key] for key in sorted(d.keys())]


new_dict = {'b': 5, 'a': 3, 'c': 4}
sorted_values = valuesort(new_dict)
print(sorted_values)
