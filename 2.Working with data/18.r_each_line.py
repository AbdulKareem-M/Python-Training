def reverse_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    for line in lines:
        print(line.strip()[::-1])


if __name__ == '__main__':
    filename = input('enter the filename')
    reverse_lines(filename)
