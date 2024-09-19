def triplets(n):
    result = []
    for a in range(1, n):
        for b in range(a, n):
            c = a + b
            if c < n:
                result.append((a, b, c))
    return result


n = 10
print(triplets(n))
