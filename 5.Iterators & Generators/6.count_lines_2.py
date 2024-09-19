import os


def count_code_lines(directory):
    total_lines = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r') as f:
                        for line in f:
                            stripped_line = line.strip()
                            if stripped_line and not stripped_line.startswith('#'):
                                total_lines += 1
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
    return total_lines


directory_path = '/path/to/directory'
print(f"Total number of lines of code: {count_code_lines(directory_path)}")
