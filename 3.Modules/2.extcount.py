import os
import sys
from collections import defaultdict


def count_extensions(directory):
    ext_count = defaultdict(int)

    try:
        # Iterate over all files in the directory
        for filename in os.listdir(directory):
            # Get the file extension
            _, ext = os.path.splitext(filename)
            if ext:
                ext_count[ext] += 1

        # Print the count of each extension
        for ext, count in ext_count.items():
            print(f"{ext}: {count}")

    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access '{directory}'.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extcount.py <directory>")
    else:
        directory = sys.argv[1]
        count_extensions(directory)
