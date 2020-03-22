fruits = ['apple', 'orange', 'watermelon']
for i in fruits:
    print(i.title()+" is tasty!")


print("\nrange (10) + if condition:")
for i in range(10):
    if not i % 2 == 0:
        print(i+1)

print("\nrange (1,5):")  # start with value of 1 till 5th index
for i in range(1, 5):
    print(i)

# num = print("1")
# print(num)
# number = range(1,10)
# print (number)

# save as list
numbers = list(range(10))
print(numbers)

# save as list with user defined increament in range
# numbers = list(range(10,2)) #dONT WORK
even_numbers = list(range(0, 11, 2))  # start with value of 2 till 11th index
print(even_numbers)

squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

# Other way

squares = [value**2 for value in range(1, 11)]
print(squares)


print(min(squares))

print(sum(squares))

print(max(squares))

# SLICING LIST
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)
# you would request indices 0 through 3, which would return elements 0, 1, and 2.
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[:-1])

print(players[2:])
print(players[-3:])
print(players[-3:5])

# Looping Through a Slice

print("Here are the first three players on my team:")

for player in players[:3]:
    print(player.title())

 # COPYING LIST

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:3:2]

# you can also use if you want to copy whole list
# friend_foods = my_foods

print("My favorite foods are:")
print(my_foods)
print("\nMy friend'sfavorite foods are:")
print(friend_foods)
