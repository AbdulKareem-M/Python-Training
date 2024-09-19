def reverse_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    for line in reversed(lines):
        print(line.rstrip())


if __name__ == '__main__':
    filename = input('enter the filename:')
    reverse_file(filename)