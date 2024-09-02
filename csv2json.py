import csv
import json

def csv2json(csv_file_path, json_file_path):
    data = []
    with open(csv_file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)  # Append the entire row as a dictionary
    
    with open(json_file_path, mode='w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    csv2json("prompts.csv", "prompts.json")