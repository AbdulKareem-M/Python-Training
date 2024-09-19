from collections import Counter


def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()


def char_frequency(text):
    return Counter(text)


def main(filename):
    text = read_file(filename)
    frequency = char_frequency(text)
    for char, count in frequency.items():
        print(f"'{char}': {count}")


if __name__ == "__main__":
    import sys
    filename = input('enter filename')
    main(filename)
