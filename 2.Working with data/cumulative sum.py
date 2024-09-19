def cumulative_sum(lst):
    cumulative_list = [sum(lst[:i+1]) for i in range(len(lst))]
    return cumulative_list


my_list = [10, 23, 34, 43, 33, 50]
result = cumulative_sum(my_list)
print(result)
