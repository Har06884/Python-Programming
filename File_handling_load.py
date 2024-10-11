# Function to load and read a text file
def load_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNoFoundError:
        return "File not found. Please check the file path."

file_path = 'quote.txt'
file_content = load_text_file(file_path)
print(file_content)
