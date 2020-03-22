import json
json_dir = 'json_files/'
text_dir = 'text_files/'
json_file = 'numbers.json'
text_file = 'numbers.json'

numbers = [2, 3, 5, 7, 11, 13]

# ============================ WRITE/DUMP
with open(json_dir + json_file, 'w') as f_obj:
    json.dump(numbers, f_obj)
    # for x in numbers:
    #   json.dump(x, f_obj)

# ============================ READ/LOAD
with open(json_dir+json_file, 'r') as f_obj:
    new_numbers = json.load(f_obj)
print(new_numbers)

# Not possible as write method only writes string
# with open(text_dir+text_file, 'w') as f_obj:
#     f_obj.write(numbers)


# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.
filename = json_dir+'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username + "!")
else: # IT will only run after try
    print("Welcome back, " + username + "!")
