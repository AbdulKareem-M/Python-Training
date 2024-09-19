import re


def grep(pattern, filename):
    with open(filename, 'r') as file:
        for line in file:
            if re.search(pattern, line):
                print(line.rstrip())


if __name__ == '__main__':
    pattern = input('enter the search pattern')
    filename = input('enter thr filename')
    grep(pattern, filename)
