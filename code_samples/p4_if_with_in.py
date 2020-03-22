# IF STATEMENT
# Python does not require an else block at the end of an if-elif chain.
# Unlike C++ or Java

cars = ['audi', 'bmw', 'subaru', 'toyota']

if not cars:
    print('Empty Car List')

if cars == []:
    print('Empty Car List')

for car in cars:
    if car == 'bmw':
        print(car.upper())
    elif cars == []:             # this condition wont run as if empty FOR LOOP won't run
        print('No car present')
    else:
        print(car.title())

age_0 = 10
age_1 = 12

if(age_0 > 1 and age_0 < age_1):
    print("\nYoung")
if(age_1 > age_0 or age_1 >= 11):
    print("Elder")

# Check presence in list
car = 'bmw'

print("\nAudi is presend in cars:- " + str('audi' in cars))
print(car.title()+" is presend in cars:- " + str(car in cars)+"\n")

# Another way

car = 'Suzuki'

if car in cars:
    print(car+' is present')
if car not in cars:
    print(car+' is not present\n')

# it does not check presence in 'for loop' as output of cars is
# overwritten by for loop
# for car in cars :
#     print (car)

# Checking Multiple List

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")
