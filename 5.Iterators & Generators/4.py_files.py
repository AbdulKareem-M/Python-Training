import os


def count_python_files(directory):
    count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                count += 1
    return count


directory_path = '/path/to/directory'
print(f"Number of Python files: {count_python_files(directory_path)}")
