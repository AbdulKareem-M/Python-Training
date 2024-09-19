x = 1


def f():
    y = x  # error,should define x as a global variable first
    x = 2
    return x + y


print(x)
print(f())
print(x)

