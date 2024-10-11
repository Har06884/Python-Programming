import csv

# Load the CSV file
try:
    with open('data.csv', 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
except FileNotFoundError:
    print("The file 'data.csv' was not found.")
    exit()

# Ask the user to enter some numbers
numbers = input("Enter some numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]

# Perform a complex calculation of modulus and multiplication
results = []
for num in numbers:
    result = (num % 5) * 3  # Example complex calculation
    results.append(result)

# Print the output to screen
print("Results of the complex calculation:")
for result in results:
    print(result)

# Ask the user to define the file name, but set the extension to .txt
file_name = input("Enter the file name to save the results (without extension): ") + ".txt"

# Save the new data to a text file
with open(file_name, 'w') as file:
    for result in results:
        file.write(str(result) + '\n')

print(f"Results have been saved to {file_name}.")
