import textwrap
import sys


def wrap_file(filename, width):
    with open(filename, 'r') as file:
        for line in file:
            wrapped_lines = textwrap.wrap(line, width)
            for wrapped_line in wrapped_lines:
                print(wrapped_line)


if __name__ == "__main__":
    filename = input('enter thee filename')
    width = int(input('enter the width'))
    wrap_file(filename, width)
