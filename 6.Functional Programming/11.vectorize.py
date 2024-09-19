def vectorize(f):
    def new_func(lst):
        return [f(x) for x in lst]
    return new_func

# Example usage:
def square(x):
    return x * x

vectorized_square = vectorize(square)
result = vectorized_square([1, 2, 3, 4, 5])
print(result)  # Output: [1, 4, 9, 16, 25]
