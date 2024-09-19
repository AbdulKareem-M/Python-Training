import os
import sys

def print_tree(directory, prefix=''):
    try:
        contents = os.listdir(directory)
    except PermissionError:
        print(f"{prefix}Permission denied: {directory}")
        return

    for i, name in enumerate(contents):
        path = os.path.join(directory, name)
        if i == len(contents) - 1:
            connector = '└── '
            new_prefix = prefix + '    '
        else:
            connector = '├── '
            new_prefix = prefix + '│   '

        print(prefix + connector + name)
        if os.path.isdir(path):
            print_tree(path, new_prefix)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 7.dirtree.py <directory>")
    else:
        directory = sys.argv[1]
        if os.path.isdir(directory):
            print(directory)
            print_tree(directory)
        else:
            print(f"{directory} is not a valid directory.")
