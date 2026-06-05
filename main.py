import csv

def read_csv(file_path):
    print(f"Reading data from {file_path}...")
    with open(file_path, mode='r', encoding='latin-1') as file:
        csv_reader = csv.reader(file)
        data = [row for row in csv_reader]
    print(f"data: {data}")

read_csv("user_details.csv")