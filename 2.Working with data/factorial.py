def fact(number):
    if number == 0:
        return True
    else:
        return number * fact(number - 1)


print(fact(4))

