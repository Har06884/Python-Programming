import csv

# Function to load and read a CSV file
def load_csv_file(file_path):
    try:
        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file)
            data = [row for row in csv_reader]
        return data
    except FileNotFoundError:
        return "File not found. Please check the file path."
'''
file_path = 'sample.csv'
csv_data = load_csv_file(file_path)
for row in csv_data:
    print(row)
'''

file_path = r'C:\Users\white\OneDrive\Desktop\Python Level 3\sample.csv'
csv_data = load_csv_file(file_path)
for row in csv_data:
    print(row)
