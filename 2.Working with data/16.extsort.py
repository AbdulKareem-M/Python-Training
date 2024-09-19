def extsort(files_input):
    return sorted(files_input, key=lambda x: x.split('.')[-1])


my_files = ['abc.txt', 'hello.py', 'flower.jpg', 'extsort.py', 'vid.mp4']
sorted_files = extsort(my_files)
print(sorted_files)