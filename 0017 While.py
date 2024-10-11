# 1. Basic Counting
# This loop prints numbers from 1 to 10
number = 1
while number <= 10:
    print(number)
    number += 1

print("\n---\n")

# 2. Infinite Loop
# This loop will keep printing "Hello, World!" until manually stopped
# Uncomment the lines below to run it
# while True:
#     print("Hello, World!")

print("\n---\n")

# 3. User Input
# This loop keeps asking the user for input until they type "exit"
user_input = ""
while user_input.lower() != "exit":
    user_input = input("Type 'exit' to stop: ")

print("\n---\n")

# 4. Using `break` to Exit Loop
# This loop prints numbers from 1 to 10, but stops if the number is 5
number = 1
while number <= 10:
    if number == 5:
        break
    print(number)
    number += 1

print("\n---\n")

# 5. Using `continue` to Skip Iteration
# This loop prints numbers from 1 to 10, but skips the number 5
number = 1
while number <= 10:
    if number == 5:
        number += 1
        continue
    print(number)
    number += 1

print("\n---\n")

# 6. Nested `while` Loops
# This loop prints a 3x3 grid of numbers
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"({i}, {j})", end=" ")
        j += 1
    print()
    i += 1
