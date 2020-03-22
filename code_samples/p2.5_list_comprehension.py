
# ======================================= LIST COMPREHENSION
line = '1 2 3 4'  # string
b = [i+i for i in line]
print(b)

line = line.split()  # now become list

# printing Sum using lc
a = [int(i) for i in line]  # returns list
print(a)
print(sum(a))

# get list of square
sqr = [i*i for i in a]
print(sqr)
