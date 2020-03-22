""""
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.""""
# MAKING LIST

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)  # prints acutal representation of Lists
# print ("List: " + bicycle) :: Not possible : Cannot concatenate String with List

# ACCESSING ELEMENT in LIST

print(bicycles[0].title())  # prints values only
print(bicycles[-1].title())  # UnderFlow in case of value smaller than start

# print(bicycles[-5].title()) :: IndexError: list index out of range(-4 to 3)
# print(bicycles[4].title()) :: IndexError: list index out of range

# ADDING AN ELEMENT IN LIST

bicycles.append('mountain')  # add a new element at End of your list
print(bicycles)

bicycles.insert(0, 'sport')  # add a new element at Any position in your list
print(bicycles)

# REMOVING AN ELEMENT FROM LIST

del bicycles[3]  # remove an element at any position from your list
print(bicycles)

bicycles.remove('cannondale')  # remove item by Value
print(bicycles)

# popped_bicycle = bicycles.pop() :: removes the Last item from the list i.e when no parameter passed
# removes the any item from the list, but it lets you work with (return) that item after removing it
popped_bicycle = bicycles.pop(0)
print(bicycles)
print("Remove item: "+popped_bicycle)


# SORTING LIST without Permanent Change
# Sorting a list alphabetically is a bit more complicated when all the values are not in lowercase

print("\nUnsorted List: ")
print(bicycles)
print("\nSorted List (Ascending): ")
print(sorted(bicycles))
print("\nSorted List (Descending): ")
print(sorted(bicycles, reverse=True))

# the sorted function Does Not changes original List
print("\nOriginal List: ")
print(bicycles)

# Reversing (not sorting) with Permanent Change
# or Invert

print("\nList:")
print(bicycles)
bicycles.reverse()
print("List is Reversed:")
print(bicycles)

bicycles.reverse()
print("List is Reversed again to remove Reverse Affect:")
print(bicycles)

# Length of List

print("Length of List : " + str(len(bicycles)))


# Storing from String in list
line = '1 2 3 4'  # string
line = line.split()  # now become list
print(line)
