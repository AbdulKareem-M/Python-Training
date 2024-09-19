import os


def findfiles(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            yield os.path.join(root, file)


for filepath in findfiles('/path/to/directory'):
    print(filepath)
