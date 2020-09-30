# https://www.youtube.com/watch?v=mclfteWlT2Q&list=PLzMcBGfZo4-kwmIcMDdXSuy_wSqtU-xDP
# Expert Python Tutorial #1 - Overview of Python & How it Works

# Python is compiled into bytecode before it is interpreted
# Compilers take high-level code and translate it into a lower-level
# An interpreter takes some kind of code, in our case bytecode, and interprets & runs that code

# Left off at 3:36 / 19:09

# This is unique to Python because it is a compiled language...
# ...here we have a class with an undefined 'bark' method
class Dog:
  def __init__(self):
    self.bark() # here we are calling a method that does not exist called 'bark'
# If I run the code at this point there will be no errors...
# In other languages, the compiler would detect this error and tell you to define
# what 'bark' is, but here, this bit of code is executed at runtime instead of compile time
# All the compiler does for us is translate the Python into bytecode, and it does
# not always check to see if the code is actually valid.  Thus, the error above is
# said to be 'only caught at runtime' and not at compile time.

# Let's look at another example in which the compiler doesn't care if the code is valid or not,
# so long as you have valid syntax
def make_class(x):
  class Cat: # we can define a class inside a function because that is how Python works; we can nest classes as deep as we want.
    def __init__(self, name):
      self.name = name

    def print_value(self):
      print(x)

  return Cat # we're returning the class 'Cat' and not an instance of the class'Cat()'

cls = make_class(10)
print(cls)
#=> <class '__main__.make_class.<locals>.Cat'>

# We see the output above because the class is being created and stored in memory

d = cls("Timmy") # this 'cls' variable is actually a class...so it's another name for Cat
d.print_value() # Here we're calling the class method
#=> 10

print(d.name) # the name of this instance of the 'Cat' class is Timmy
#=> Timmy

for i in range(10):
  def show(): # i can put a function inside a for loop
    print(i*2)

  show() # this will run each time the loop runs...
show()  # this will only run once on the final item in the range, but it is aware
        # of the existence of 'show()' inside a deeper scope it is not a part of.
        # BUT 'show()' must be declared on a line ABOVE wherever it is being called
        # or it will not run and will generate an 'is-not-defined' error

# Any argument defined outside a function can be used inside a function
def func(x):
  if x == 1:
    def rv():
      print("X is equal to 1")

  else:
    def rv():
      print("X is not equal to 1")

  return rv

new_func = func(1)
new_func()
#=> X is equal to 1

another_func = func(2)
another_func()
#=> X is not equal to 1

# Everything in Python is an object so each thing has its own unique memory address
# so as long as we can reference that we can use it
print(id(new_func))
#=> s.thing like "140175176829808" <-this is the memory address

import inspect # This is the inspect module
# it can show us some pretty cool things because of the fact that all of our
# python objects are live
print(inspect.getmembers(new_func()))
#=> [('__bool__', <method-wrapper '__bool__' of NoneType object at 0x9d4380>),et.al

# we can get the sourcecode of a specific method, function, class, or other object
print(inspect.getsource(new_func))
#=>     def rv():
#=>       print("X is equal to 1")]

from queue import Queue
print(inspect.getsource(Queue))
# this will show us all the code that Python has used to create the object or class,
# in this case it is the Queue module
