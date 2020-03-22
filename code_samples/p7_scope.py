# ======================= Local scope 

def myfunc():
  x = 1
  print(x)
myfunc()
# ====================== Scope of nested function
def myfunc():

  """
  If you operate with the same variable name inside and outside of a function,
  Python will treat them as two separate variables, one available in the 
  global scope (outside the function) and one available in the local scope 
  (inside the function)
  """

  x = 2

  def myinnerfunc():
    x = 3
    print(x)
  myinnerfunc()
  print(x)

myfunc()
# ====================== Global keyword

def myfunc():
  """
  Accessible outside also
  """
  global x
  x = 4

myfunc()
print(x)
