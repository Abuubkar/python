
integer = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

map_data = list(map(lambda x: x % 2 == 0, integer))

filter_data = list(filter(lambda x: x % 2 == 0, integer))
print(map_data)
print(filter_data)

# random.randin()
# random.randin(start,end)
# random.choice(list)
# ord(char)