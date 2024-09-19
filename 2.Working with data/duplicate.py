def dups(lst):
    seen = set()
    duplicates = set()

    for num in lst:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)


# Example usage:
my_list = [1, 1, 3, 4, 2, 5, 6, 6, 7, 8]
print(dups(my_list))
