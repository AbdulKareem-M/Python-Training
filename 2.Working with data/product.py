def product(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result


lis = [2, 3, 5, 7]

result = product(lis)
print(result)
