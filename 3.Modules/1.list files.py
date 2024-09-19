import os


def list_files(directory):
    try:
        # Get the list of all files and directories
        files = os.listdir(directory)

        # Filter out directories, only keep files
        files = [f for f in files if os.path.isfile(os.path.join(directory, f))]

        print(f"Files in '{directory}':")
        for file in files:
            print(file)
    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access '{directory}'.")


# Example usage
directory_path = input("Enter the path of the directory: ")
list_files(directory_path)
