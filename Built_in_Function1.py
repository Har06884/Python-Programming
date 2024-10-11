import random
import math

# Arithmatic Function
def arithmetic_operations(a,b):
    print(f"Sum: {a + b}")
    print(f"Diference: {a - b}")
    print(f"Product: {a * b}")
    print(f"Quotient: {a / b}")
    print(f"Power: {a ** b}")
    print(f"Modulus: {a % b}")

# Random and Math Modules
def random_math_function():
    print(f"Random integer between 1 and 10: {random.randint(1,10)}")
    print(f"Random float between 0 and 1: {random.random()}")
    print(f"Square root of 16: {math.sqrt(16)}")
    print(f"Factorial of 5: {math.factorial(5)}")
    print(f"Cosine of 0: {math.cos(0)}")
    print(f"Logarithm base of 10 of 100: {math.log10(100)}")

# String Handling
def string_handling(s):
    print(f"Uppercase: {s.upper()}")
    print(f"Lowercase: {s.lower()}")
    print(f"Title Case: {s.title()}")
    print(f"Reversed: {s[::-1]}")
    print(f"Length: {len(s)}")
    print(f"Replace 'e' with '@': {s.replace('e', '@')}")

def general_functions():
    print(f"Absolute value -10: {abs(-10)}")
    print(f"Maximum of [1,2,3]: {max([1, 2, 3])}")
    print(f"Minimum of [1,2,3]: {min([1, 2, 3])}")
    print(f"Sum of [1,2,3]: {sum([1, 2, 3])}")
    print(f"Round of 3.14159: {round(3.14159, 2)}")
    print(f"Sorted list [3,1,2]: {sorted([3, 1, 2])}")

def main():
    a = 10
    b = 5
    s = "Hello, World!"

    print("Arithmetic Operations:")
    arithmetic_operations(a, b)

    print("\nRandom and Math Functions:")
    random_math_function()

    print("\nString Handling:")
    string_handling(s)

    print("\nGeneral Functions:")
    general_functions()

if __name__ == "__main__":
    main()

    
