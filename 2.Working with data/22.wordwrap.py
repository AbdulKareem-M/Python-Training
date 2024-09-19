import textwrap
import sys


def word_wrap(filename, width):
    with open(filename, 'r') as file:
        for line in file:
            wrapped_lines = textwrap.fill(line, width, break_long_words=False, break_on_hyphens=False)
            print(wrapped_lines)


if __name__ == "__main__":
    filename = input('enter thee filename')
    width = int(input('enter the width'))
    word_wrap(filename, width)
