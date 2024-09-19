import os


def extsort(files):
    return sorted(files, key=lambda x: os.path.splitext(x)[1])


files = ['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c']
sorted_files = extsort(files)
print(sorted_files)

