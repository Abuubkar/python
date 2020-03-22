# Dictionaries (like hash map)
# A dictionary in Python is a collection of key-value pairs
alien_0 = {'color': 'green', 'points': 5}

# Good practice is writing alien_0.get(key,default value if not find)
# as better if not found will return default value unlike alien_0[key]
print(alien_0['color'])
print(alien_0['points'])

# Adding new Elements
alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# Modifying Value
alien_0['color'] = 'yellow'

print("\nThe alien is now " + alien_0['color'] + ".")

# Deleting value
del alien_0['points']

print(alien_0)
print('\n')

# ============================================ Looking key-value
user_0 = {
    'username': 'fermi',
    'first': 'enrico',
    'last': 'fermi',
}

for obj in user_0.items():
    print(obj)
print('\n')

for key, value in user_0.items():
    print("Key: " + key)
    print("Value: " + value)
print('\n')

for key in user_0.keys():
    print("Key: " + key)
print('\n')

for value in user_0.values():
    print("Value: " + value)
print('\n')

print('Sorted Keys: ')
for key in sorted(user_0.keys()):
    print(key.title())
print('\n')

print("Set:")
for value in set(user_0.values()):
    print(value.title())
print("\n")

# ======================= Dictionary in Array ============================
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
print("\n")
# Making 30 Aliens
# Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Show the first 5 aliens:
for alien in aliens[:5]:
    print(alien)
print("...\n")
# Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))

# ======================= List in Dictionary ============================
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

# Or
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:          # Language is Value
        print("\t" + language.title())

# ======================= Dictionary in Dictionary ============================
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
