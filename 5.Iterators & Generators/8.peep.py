import itertools


def peep(iterator):
    # Convert the iterator to a tee object with two independent iterators
    iterator1, iterator2 = itertools.tee(iterator)
    # Get the first element from the first iterator
    first_element = next(iterator1)
    return first_element, iterator2


iterable = iter([1, 2, 3, 4, 5])
first, new_iter = peep(iterable)
print("First element:", first)
print("Remaining elements:", list(new_iter))
