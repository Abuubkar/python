

try:
    answer = int(input("Enter two Value for Division:-\n")) / int(input())



except TypeError as err:
    
    print("Error: " + str(err))
except ZeroDivisionError as err:
    print("Error: "+str(err))

except ValueError as err:
    print("Error: Enter Integer only ")
    
except Exception as ex:
    print('TYPE ' + str(ex))
    ex.__traceback__()
    
else: # It will only run after TRY
    print(round(answer))

"""
Things in try cannot be accessed in Finally
So, 
    Use "else"
"""

x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero")

x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed")
