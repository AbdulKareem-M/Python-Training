import csv


def parse_csv(file_path, delimiter=',', comment_char='#'):
    data = []
    with open(file_path, mode='r', newline='') as file:
        csv_reader = csv.reader(file, delimiter=delimiter)
        for row in csv_reader:
            if not row or row[0].startswith(comment_char):
                continue
            data.append(row)
    return data


file_path = 'example.csv'
parsed_data = parse_csv(file_path, delimiter=';', comment_char='#')
for row in parsed_data:
    print(row)
