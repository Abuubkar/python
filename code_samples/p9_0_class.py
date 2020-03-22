# private data member does not call GETTER AND SETTER
#
# public data member do call GETTER AND SETTER and is MUST needed other wise
# will not let assignment or retrival via call:
# self.data = d or print (self.data) 
# in such case you would have to use :
# self._data = d or print (self._data)

#SELF._MEMBER will not call getter and setter # saves from looping is getter/setter
#SELF.MEMBER will call getter and setter
# getter and setter should have same function name as DATA MEMBER


############################
"""
public data member banya tu uska private version bi use kr skta 
yani fix ni hoti access

but agar private rkh do to public ni kr skte
cause is case me getter / setter bilkul ni honay chahiye
ku k base type private hai
upar walay case me wo ignore kr deta hai
"""


"""
For GETTER only:
public data member banya tu uska private version bi use kr skta 
and vice versa

bo = Bo()
print("public")
print(bo.bill)
print("private")
print(bo._bill)

For SETTER only
public data member banya to uska private version bi use kr skta like watt public banaya tha
but
private data member banya to uska public version ni use kr skta like bill private banaya tha
ku k jab public krte assignment par setter call hota jabke private ka setter not possible

# bo.bill = 10  # will call setter but as it is private by constructor so will give error 
bo._bill = 10
bo.watt = 10  # will call setter but as it is public by constructor so will not give error
bo._watt = 100 # while private assignment will work by ignoring setter

"""
############################
class Dog():
    """A simple attempt to model a dog."""
    # name="" 
    # age =0  
    # Even if it is not declared line no 11/12 will automaticall make is
    #  in Constructor __init__
    def __init__(
            self, name, age):
        """
        ==>(Constructor)<==
        Initialize name and age attributes.
        """
        self.name = name
        self.age = age
        
        #name = n
        #age = a
        #self.name = n
        #self.age = a

    def sit(
            self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")
    
    
    def roll_over(
            self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")


my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()

# Even if not argument is passed you need to set 
#   SELF in parameter of module
