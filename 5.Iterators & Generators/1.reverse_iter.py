class reverse_iter:
    def __init__(self, lst):
        self.lst = lst[::-1]  # Reverse the list using slicing
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.lst):
            raise StopIteration
        result = self.lst[self.index]
        self.index += 1
        return result


my_list = [1, 2, 3, 4, 5]
rev_iter = reverse_iter(my_list)

for item in rev_iter:
    print(item)
