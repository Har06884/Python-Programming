import csv
import random

# Define the data field and generate sample data

data =[
    {"Name": "Alice", "Age": random.randint(20,40), "City": "Ebbw Vale"},
    {"Name": "Bob", "Age": random.randint(20,40), "City": "Tredegar"},
    {"Name": "Charlie", "Age": random.randint(20,40), "City": "Newport"},
    {"Name": "David", "Age": random.randint(20,40), "City": "Caerphilly"},
    {"Name": "Eve", "Age": random.randint(20,40), "City": "Llantrisant"},
    {"Name": "Frank", "Age": random.randint(20,40), "City": "Port Talbot"}
]

# Define the CSV file name
csv_file = "Student.csv"

# Write data to CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["Name","Age","City"])
    writer.writeheader()
    for row in data:
        writer.writerow(row)

print(f"Data have been Saved to {csv_file}")
