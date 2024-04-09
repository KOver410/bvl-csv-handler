import csv
import os


current_file_path = os.getcwd()

file_path = f'{current_file_path}/Relationship.csv'
result_path = f'{current_file_path}/result.csv'

def load_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            id_str = row[0].split()[0]
            data.append(id_str)
    return data

def csv_generator(file, data):
    with open(file, 'w', newline='') as file:
        writer = csv.writer(file)
        for item in data:
            writer.writerow([item])

#run
csv_data = load_csv(file_path)
print(csv_data)
csv_generator(result_path,csv_data)



