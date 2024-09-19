def head(filename, n=3):
    with open(filename, 'r') as file:
        for _ in range(n):
            line = file.readline()
            if not line:
                break
            print(line.rstrip())


def tail(filename, n=3):
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines[-n:]:
            print(line.rstrip())


if __name__ == '__main__':
    filename = input('enter the file name')
    head(filename)
    tail(filename)
