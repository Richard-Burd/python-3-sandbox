# this file is to explain nested function calls a little bit better than they
# are in the "/expert.py" file located in this directory.

def outer_function(x):
  def inner_function(x):
    print(f'get inside with a {x}!')

  return inner_function

zelda = outer_function("key")
zelda("key")
#=> get inside with a key!

# Everything in Python is an object so each thing has its own unique memory address
# so as long as we can reference that we can use it
print(id(zelda))
#=> s.thing like "140175176829808" <-this is the memory address

import inspect # This is the inspect module
# it can show us some pretty cool things because of the fact that all of our
# python objects are live
print(inspect.getmembers(zelda(100)))
#=> [('__bool__', <method-wrapper '__bool__' of NoneType object at 0x9d4380>),et.al

# we can get the sourcecode of a specific method, function, class, or other object
print(inspect.getsource(zelda))
#=>     def inner_function(x):
#=>       print(f'get inside with a {x}!')]
