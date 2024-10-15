#car.py used as a object

#Define a class named 'Car'
class Car:
    # Constructor method to initialise object
    def __init__(self, make, model, year, fuel_capacity, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_capacity = fuel_capacity #in liters
        self.fuel_level = 0 # in liters
        self.mileage = mileage #in km/l

    # Method to display car detail
    def display_info(self):
        print(f"Car: {self.year} {self.make} {self.model}")

    # Method to simulate starting the car
    def start_engine(self):
        if self.fuel_level > 0:
            print(f"The {self.make} {self.model}'s engine has started.")
        else:
            print(f"The {self.make} {self.model}'s has no fuel.")

    def refuel(self, liters):
        if liters <= 0:
            print(f"Please enter a valid amount of fuel to refuel.")
        elif self.fuel_level + liters > self.fuel_capacity:
            print("Cannot refuel beyond fuel capacity")
        else:
            self.fuel_level += liters
            print(f"Refueled {liters} liters. Current fuel level: {self.fuel_level} liters.")

    def drive(self, distance):
        required_fuel = distance / self.mileage
        if required_fuel <= self.fuel_level:
            self.fuel_level -= required_fuel
            print(f"Drove {distance} km. Remaining fuel: {self.fuel_level:.2f} liters")
        else:
            print("Not enough fuel to drive the distance!")

    def maintenance_check(self):
        print(f"Performing maintenance check on {self.make} {self.model}.")
        if self.year < 2022:
            print("Maintenance required: Oil change, Tire rotation")
        else:
            print("Maintenance required: MOT Required by law!")



        
