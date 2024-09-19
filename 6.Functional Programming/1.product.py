def product(x, y):
    # Base case: if y is 0, the product is 0
    if y == 0:
        return 0
    # If y is positive, add x to the product of x and (y-1)
    elif y > 0:
        return x + product(x, y - 1)
    # If y is negative, subtract x from the product of x and (y+1)
    else:
        return -product(x, -y)


print(product(5, 3))  # Output: 15

