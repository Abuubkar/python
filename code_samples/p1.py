name = " 'ada's lovelace' "
#name = ' "ada lovelace" '
# name = "ada "+"lovelace" is equal to name = "ada " "lovelace"
print(name.title())

print(name.strip())  # removes left and right space
print(name.rstrip())
print(name.lstrip())

print(10 ** 2)  # sqaure
print(10 ** 3)  # cube

print(0.1 + 0.1)  # no precision error
print(0.1 + 0.2)  # precision error will SOLVE later

num = 10
# print(name + 10) :: TypeError: can only concatenate str (not "int") to str
# print(name + num) :: TypeError: can only concatenate str (not "int") to str
print(name.title().lstrip() + "age is " + str(num))

# you can print Integer only if not concatenated with string
print(num)
print(10)
# import this :: Zen of Python

# help(function)
# dir(function)
# string.find(str,start)
