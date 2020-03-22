class Car(
    
):
    """A simple attempt to represent a car."""
    
    def __init__(
            self, make, model, 
            year):
        
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


    def get_descriptive_name(
            self):
        
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()


    def read_odometer(
            self):
        
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")


    def update_odometer(
            self, mileage):
        
        """
        Set the odometer reading to the given value.
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


    def increment_odometer(
            self, miles):
        
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


    def fill_gas_tank(
            self):
        
        """Filling gas tanks."""
        print("This car's gas tank is filled!")


# Check p8 file for working

# my_new_car = Car('audi', 'a4', 2016)
# my_tesla = ElectricCar('tesla', 'model s', 2016)

# print(my_new_car.get_descriptive_name())

# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

# my_new_car.update_odometer(100)
# my_new_car.read_odometer()

# my_new_car.increment_odometer(20)
# my_new_car.read_odometer()

# print(my_tesla.get_descriptive_name())
# my_tesla.fill_gas_tank()
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()
