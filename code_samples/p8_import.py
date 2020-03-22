# ===================== IMPORT


# Import Modules
import p7 as p
"""you need to call each function by name with using the dot
notation."""

p.describe_pet("Dog","Jack")
#p7 cannot be used as it is assigned to 'p'


# Import function
from p7 import build_profile as bp , print_models
"""you can call each function by name without using the dot
notation
Imports All Functions from Module [from p7 import *] """ 

# build_profile is not possible
bp("Abubakar", "Khawaja", Age=21)
print_models(['iphone case', 'robot pendant', 'dodecahedron'],['Samsaung case'])


# two imports are not possible from same file


print("\n")
# Import Class
from p9_1 import Car
from p9_2 import ElectricCar

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()



print("\n")
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
