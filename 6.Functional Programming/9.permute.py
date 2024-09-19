def permute(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]

    permutations = []
    for i in range(len(lst)):
        current = lst[i]
        remaining = lst[:i] + lst[i + 1:]
        for p in permute(remaining):
            permutations.append([current] + p)
    return permutations


data = [1, 2, 3]
result = permute(data)
for p in result:
    print(p)
