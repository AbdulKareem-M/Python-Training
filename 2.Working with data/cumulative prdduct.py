# normal product function

def cumulative_product(lst):
    result = 1.0
    for num in lst:
        result *= num
    return result


my_list = [12, 34, 32, 11]
result = cumulative_product(my_list)
print(result)

