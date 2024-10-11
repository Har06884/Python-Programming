# Constants
PI = 3.14159
GRAVITY = 9.81

# Global Variable
global_counter = 0

def calculate_area_of_circle(radius):
    # Local Variable
    area = PI * (radius ** 2)
    return area

def increment_counter():
    global global_counter
    global_counter += 1

def main():
    # Local Variable
    #radius = float(input("Please enter a number: "))
    radius = 5
    area = calculate_area_of_circle(radius)
    print(f"The area of a circle with radius {radius} is {area}")

    increment_counter()
    print(f"Global counter after increment: {global_counter}")

if __name__ == "__main__":
    main()
