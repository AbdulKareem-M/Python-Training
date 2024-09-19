import time


def profile(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken by {func.__name__}: {end_time - start_time:.6f} seconds")
        return result

    return wrapper


# Example usage:
@profile
def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total


result = example_function(1000000)
print(f"Result: {result}")
