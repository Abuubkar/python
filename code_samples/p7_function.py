# ========================== User defined function
def greet_user():
    """Display a simple greeting."""
    print("Hello!")


greet_user()

# ========================== User defined parameterized function
"""Display information about a pet."""


def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


# ========================== User defined function with Positional Argument
"""Positional argument is based on the order of the arguments provided."""

describe_pet('hamster', 'harry')

# ========================== User defined function with Keyword Argument
# Only difference is Funtion Call
"""Keyword argument is a name-value pair that you pass to a function."""
""""Hence order does not matters"""
describe_pet(animal_type='hamster', pet_name='harry')

# ========================== User defined function with Default Argument
"""In Default argument, Argument for a parameter is provided in the function call"""


def describe_pet1(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet1(pet_name='willie')

# ========================== User defined function with Optional Argument
"""In Default argument, Argument for a parameter is provided in the function call"""


def describe_pet2(pet_name="", animal_type=''):
    if pet_name == "" and animal_type == "":
        print("\nI don't own pet stupid!\n")
        return      # You cannot use BREAK to quit function
    else:
        print("\nI have a " + animal_type + ".")
        print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet2()

# ========================== User defined function with Arbitrary Aragument
"""
The asterisk in the parameter name *toppings tells Python to make an
empty tuple
"""

# Case 1 :- Only Value
# * tells only Value is coming


def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# OR
print("\n")
# Case 2 :- Key + Value
# ** tells key and a value is coming


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein',
                             location='princeton', field='physics')
for key, value in user_profile.items():
    print(key.title() + ": " + value.title())


# ========================================= Nested Function
def myfunc():
    x = 300

    def myinnerfunc():
        print(x)
    myinnerfunc()


myfunc()


# ========================== Example

# # A dog named Willie.
# describe_pet1('willie')
# describe_pet1(pet_name='willie')
# # A hamster named Harry.
# describe_pet('harry', 'hamster')
# describe_pet(pet_name='harry', animal_type='hamster')
# describe_pet(animal_type='hamster', pet_name='harry')


# ========================= Returning Value
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print("\n"+musician)

# ========================= Returning Dictionary


def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix', age=27)
print(musician)


# ================================ Passing List
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "\nHello, " + name.title() + "!"
        print(msg)


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

print("\n")
# ==================================== Modifying list
# List by default is PASSED BY REFFERENCE
# print_models(unprinted_designs[:], completed_models)
# Use this to send copy of "unprinted_designs[:]"


def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
