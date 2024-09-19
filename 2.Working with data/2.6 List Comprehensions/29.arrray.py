def arr(rows, cols):
    return [[None for _ in range(cols)] for _ in range(rows)]


rows,cols = 4,5
array = arr(rows,cols)
for row in array:
    print(row)