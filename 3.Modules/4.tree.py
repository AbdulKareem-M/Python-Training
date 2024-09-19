import os


def print_tree(directory, prefix=""):
    try:
        # List all files and directories in the given directory
        items = os.listdir(directory)
        items.sort()

        for index, item in enumerate(items):
            item_path = os.path.join(directory, item)
            # Check if it's the last item in the directory
            is_last = index == len(items) - 1

            # Print the current item
            if is_last:
                print(prefix + "└── " + item)
                new_prefix = prefix + "    "
            else:
                print(prefix + "├── " + item)
                new_prefix = prefix + "│   "

            # If the item is a directory, recursively print its contents
            if os.path.isdir(item_path):
                print_tree(item_path, new_prefix)

    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access '{directory}'.")


if __name__ == "__main__":
    directory_path = input("Enter the path of the directory: ")
    print_tree(directory_path)
