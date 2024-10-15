# Define a class named 'Car'
class Car:
    # Constructor method to initialise object
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # Method to display car detail
    def display_info(self):
        print(f"Car: {self.year} {self.make} {self.model}")

    # Method to simulate starting the car
    def start_engine(self):
        print(f"The {self.make} {self.model}'s engine has started.")

# Create an object
my_car = Car("Toyota", "Corolla", 2020)
my_car2 = Car("Honda", "Civic", 2021)

# Call methods on the object
my_car.display_info()
my_car.start_engine()

my_car2.display_info()
my_car2.start_engine()
