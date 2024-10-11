import os
import csv

# Function to load and read all CSV files from a directory
def load_all_csv_files(directory_path):
    csv_files_data = {}
    try:
        for filename in os.listdir(directory_path):
            if filename.endswith('.csv'):
                file_path = os.path.join(directory_path, filename)
                with open(file_path, mode='r') as file:
                    csv_reader = csv.reader(file)
                    data = [row for row in csv_reader]
                    csv_files_data[filename] = data
        return csv_files_data
    except FileNotFoundError:
        return "Directory not found. Please check the directory path."

# Example usage
directory_path = r'C:\Users\white\OneDrive\Desktop\Software Development Assignment'  # Replace with your directory path
csv_files_data = load_all_csv_files(directory_path)
for filename, data in csv_files_data.items():
    print(f"Contents of {filename}:")
    for row in data:
        print(row)
    print("\n")
