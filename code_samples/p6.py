# ================================= Input function

# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

# STRING is returned so change to INT
# Explicitly if needed

# age = int(input("How old are you? ")) 
# print(age) 

# ================================= While loops

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "

# message = ""
# while message != 'quit':
#     message = input(prompt)
#     print(message)

# ====================================================== Break

# active = True
# while active:
#  message = input(prompt)
#  if message == 'quit':
#   active = False
#   break
#  else:
#   print(message)

# ================================= Continue

# current_number = 0
# while current_number < 10:
#  current_number += 1
#  if current_number % 2 == 0:
#   continue
#  print(current_number)

# ==================== Printing list using loops 

# Start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# ==================== Removing using loops
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
# print(pets[1])
while 'cat' in pets:
 pets.remove('cat')
print(pets)

# ==================== Filling list using loops via Input

# Set a flag to indicate that polling is active.
polling_active = True
responses = {}
while polling_active:
 # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

# Store the response in the dictionary:
    responses[name] = response

# Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
