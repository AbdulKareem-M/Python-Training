import csv


def parse_csv(file_name):
    data = []
    with open(file_name, mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data


file_name = 'example.csv'
parsed_data = parse_csv(file_name)
for row in parsed_data:
    print(row)
