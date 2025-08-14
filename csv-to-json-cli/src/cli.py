import argparse
import os
import json
import csv
from utils import csv_to_json, data_to_csv

def main():
    parser = argparse.ArgumentParser(description='Convert CSV files to JSON format.')
    parser.add_argument('csv_file', type=str, help='Path to the input CSV file')
    parser.add_argument('json_file', type=str, help='Path to the output JSON file')
    
    args = parser.parse_args()

    if not os.path.isfile(args.csv_file):
        print(f"Error: The file {args.csv_file} does not exist.")
        return

    try:
        csv_to_json(args.csv_file, args.json_file)
        print(f"Successfully converted {args.csv_file} to {args.json_file}.")
    except Exception as e:
        print(f"An error occurred: {e}")

def create_sample_csv_and_convert():
    """
    Create a sample CSV file from Python data and convert it to JSON.
    """
    sample_data = [
        {"name": "Alice", "age": 30, "city": "New York"},
        {"name": "Bob", "age": 25, "city": "London"},
        {"name": "Charlie", "age": 35, "city": "Paris"}
    ]
    csv_file = "sample.csv"
    json_file = "sample.json"
    data_to_csv(sample_data, csv_file)
    print(f"Sample CSV file '{csv_file}' created.")
    csv_to_json(csv_file, json_file)
    print(f"Converted '{csv_file}' to '{json_file}'.")

if __name__ == '__main__':
    # Uncomment below to run the sample data conversion
    # create_sample_csv_and_convert()
    main()