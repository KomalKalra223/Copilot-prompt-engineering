def csv_to_json(csv_file, json_file):
    import csv
    import json

    with open(csv_file, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]

    with open(json_file, mode='w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def read_csv(csv_file):
    import csv

    with open(csv_file, mode='r', encoding='utf-8') as file:
        return list(csv.reader(file))

def write_json(data, json_file):
    import json

    with open(json_file, mode='w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def data_to_csv(data, csv_file):
    """
    Write a list of dictionaries to a CSV file.
    Each dict should have the same keys.
    """
    import csv
    if not data:
        raise ValueError("Data list is empty.")
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)