"""
a => Append                :: if file is not present will create file
w => Write                 :: if file is not present will create file
r => Read                  :: if file is not present will give error
x => w + r and create file :: if file is present will give error
b => binary mode
"""


# ======================= Reading  from file

# Absolute Path :-
# file_path = 'C:\Users\abuba\Documents\PYTHON TUts\pyExample>python -u "c:\Users\abuba\Documents\PYTHON TUts\pyExample\text_files\filename.txt'
# with open(file_paths) as file:

file_path = "text_files/pi_digits.txt"

"""
Two ways to open File 
-> with Keyword (requires indentation / automatically closes file)
-> Assignment to object

"""

# ================ Read whole content and Character by Character
with open('text_files/pi_digits.txt') as file:
    """Print Whole Content"""
    content = file.read()
    print(content.rstrip())

    """Read Character by Character"""
    print('\nWithout rstrip:')
    for char in content:
        print(char.strip())


print('\nUsing rstrip:')
file = open(file_path)
pi_string = ''

# ========================== Read line by line
"""Read Line by line"""
for line in file:
    pi_string += line.rstrip()

print("pi = "+pi_string)
print("size = " + str(len(pi_string)))


# ========================== Readlines to read line by line
print('\nUsing strip:')
file = open(file_path)
pi_string = ''

lines = file.readlines()
print(lines)

for line in lines:
    pi_string += line.strip()

print("pi = "+pi_string)
print("size = " + str(len(pi_string)))

file.close()
