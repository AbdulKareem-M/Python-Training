def lensort(lst):
    return sorted(lst, key=len)


strings = ['apple', 'mango', 'papaya', 'guava', 'peach', 'fig']
result = lensort(strings)
print(result)