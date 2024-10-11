# Arithmetic Operations in Python

# Function to perform addition
def addition(a, b):
    # Adding two numbers
    result = a + b
    # Printing the result of the addition
    print(f"Addition: {a} + {b} = {result}")
    return result

# Function to perform subtraction
def subtraction(a, b):
    # Subtracting the second number from the first
    result = a - b
    # Printing the result of the subtraction
    print(f"Subtraction: {a} - {b} = {result}")
    return result

# Function to perform multiplication
def multiplication(a, b):
    # Multiplying two numbers
    result = a * b
    # Printing the result of the multiplication
    print(f"Multiplication: {a} * {b} = {result}")
    return result

# Function to perform division
def division(a, b):
    # Checking if the divisor is not zero to avoid division by zero error
    if b != 0:
        # Dividing the first number by the second
        result = a / b
        # Printing the result of the division
        print(f"Division: {a} / {b} = {result}")
        return result
    else:
        # Printing an error message if the divisor is zero
        print("Error: Division by zero is not allowed.")
        return None

# Function to perform modulus operation
def modulus(a, b):
    # Calculating the remainder of the division of the first number by the second
    result = a % b
    # Printing the result of the modulus operation
    print(f"Modulus: {a} % {b} = {result}")
    return result

# Function to perform exponentiation
def exponentiation(a, b):
    # Raising the first number to the power of the second number
    result = a ** b
    # Printing the result of the exponentiation
    print(f"Exponentiation: {a} ** {b} = {result}")
    return result

# Function to perform floor division
def floor_division(a, b):
    # Checking if the divisor is not zero to avoid division by zero error
    if b != 0:
        # Performing floor division (division that rounds down to the nearest integer)
        result = a // b
        # Printing the result of the floor division
        print(f"Floor Division: {a} // {b} = {result}")
        return result
    else:
        # Printing an error message if the divisor is zero
        print("Error: Division by zero is not allowed.")
        return None

# Main function to demonstrate the arithmetic operations
def main():
    # Defining two numbers to use in the operations
    a = 10
    b = 3

    # Introduction message
    print("Let's learn about basic arithmetic operations in Python!\n")
    
    # Demonstrating each arithmetic operation
    addition(a, b)
    subtraction(a, b)
    multiplication(a, b)
    division(a, b)
    modulus(a, b)
    exponentiation(a, b)
    floor_division(a, b)

# Ensuring the main function runs when the script is executed
if __name__ == "__main__":
    main()
