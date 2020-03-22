# TUPLE (list but use Circle Bracket)

dimensions = (200, 50)

print(dimensions)
print(dimensions[0:2])  # will give error if slice is inside circle bracket
print(dimensions[0])
print(dimensions[1])

#  you can’t modify a tuple, you can assign a new value to a variable
#  that holds a tuple
#  dimensions[0]='appl'
#  not possible but following is possible

# Overwrite is Possible
dimensions = (400, 100, 50)

print(dimensions)
