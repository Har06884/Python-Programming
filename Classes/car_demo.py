# car_demo.py
from car import Car

my_car3 = Car("Ford", "Mustang", 2022, 60, 12) #60 liter fuel capacity, 12km/l mileage


# Call Methods on the car object
my_car3.display_info()
my_car3.refuel(50)
my_car3.start_engine()
my_car3.drive(300)
my_car3.maintenance_check()
