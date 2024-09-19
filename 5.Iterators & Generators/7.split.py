import sys
import os


def split_file(filename, n):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        file_count = 0
        for i in range(0, len(lines), n):
            file_count += 1
            with open(f"{filename}_part{file_count}.txt", 'w') as new_file:
                new_file.writelines(lines[i:i + n])

        print(f"File split into {file_count} parts.")
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python split.py <number_of_lines> <filename>")
    else:
        try:
            n = int(sys.argv[1])
            filename = sys.argv[2]
            split_file(filename, n)
        except ValueError:
            print("The first argument must be an integer.")
