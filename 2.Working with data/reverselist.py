def reverse(lst):
    left, right = 0, len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1


ln = [1, 2, 3, 4, 5, 6]

reverse(ln)
print(ln)
