def center_align(filename, width):
    with open(filename, 'r') as file:
        lines = file.readlines()
    for line in lines:
        print(line.strip().center(width))


if __name__ == "__main__":
    filename = input("Enter the filename: ")
    width = int(input("Enter the width for alignment: "))
    center_align(filename, width)
