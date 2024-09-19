import sys


def print_long_lines(filenames):
    for filename in filenames:
        try:
            with open(filename, 'r') as file:
                for line in file:
                    if len(line) > 40:
                        print(line.strip())
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except Exception as e:
            print(f"An error occurred while processing {filename}: {e}")


if __name__ == "__main__":
    filename = input('enter the filename')
    print_long_lines(filename)

