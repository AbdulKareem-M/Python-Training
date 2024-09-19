import os


def count_lines_of_code(directory):
    total_lines = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r') as f:
                        total_lines += sum(1 for line in f)
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
    return total_lines


directory_path = '/path/to/directory'
print(f"Total number of lines of code: {count_lines_of_code(directory_path)}")