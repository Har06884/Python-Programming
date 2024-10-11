# Define the text you want to save

text_to_save = '''In the heart of darkness, whispers of ancient power beckoned,
Steel met sorcery in a cataclysmic dance of destiny.
Honor and ambition, two sides of a tarnished coin,
In the end, only echoes of shattered brotherhood remained.'''

# Open a file in write mode
with open("output.txt", "w") as file:
    # Write the text to the file
    file.write(text_to_save)

print("Text has been saved to file!")
