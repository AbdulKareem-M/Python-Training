def izip(*iterables):
    iterators = [iter(it) for it in iterables]
    while True:
        try:
            yield tuple(map(next, iterators))
        except StopIteration:
            return


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
izip(list1, list2)
print(izip)
