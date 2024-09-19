import os
import time


def list_files_with_details(directory):
    try:
        # Iterate over all files in the directory
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)

            # Check if it's a file
            if os.path.isfile(file_path):
                # Get file size
                file_size = os.path.getsize(file_path)

                # Get last modification time
                mod_time = os.path.getmtime(file_path)
                mod_time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mod_time))

                # Print details
                print(f"{filename}\t{file_size}\t{mod_time_str}")

    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access '{directory}'.")


# Example usage
directory_path = input("Enter the path of the directory: ")
list_files_with_details(directory_path)
