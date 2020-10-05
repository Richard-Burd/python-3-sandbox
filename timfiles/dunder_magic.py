# https://www.youtube.com/watch?v=z11P9sojHuM&list=PLzMcBGfZo4-kwmIcMDdXSuy_wSqtU-xDP&index=2
# Expert Python Tutorial #2 - Dunder/Magic Methods & The Python Data Model


class Dog:
  def __init__(self, name):
    self.name = name

d = Dog("Fido")

# by default we get the memory address location of this object because we have
# not told the object what to do when we print it
print(d)
#=> <__main__.Person object at 0x7f60d1aa5780>

# To get meaningful information, we need to implement a 'Dunder' method AKA magic method

class Person:
  def __init__(self, name):
    self.name = name

  # This is the 'Dunder' method, it allows us to define the string representation
  # of an object inside the actual object:
  def __repr__(self):                  # --------------------- Data model method
    return f"My Person({self.name})"

  # This data model method will tell Python how to handle multiplication operations
  # on an object that is of the data type Person...i.e. an instance of the Person class
  def __mul__(self, x):                # --------------------- Data model method
    if type(x) is not int:
      raise Exception("invalid argument, must be an integer!")

    self.name = "^" + ("*" + self.name + "*") * x + "^"

  # Whenever this Person class is called as if it were a function, this method
  # will handle that call for the Person class...thus, p(22) below returns:
  # #=> called this function 22
  def __call__(self, y):               # --------------------- Data model method
    print("called this function", y)

  # This data model method will tell Python what to do when the length (len) is
  # called on the Person class; in the example below, the string "four" has 4 items
  def __len__(self):                   # --------------------- Data model method
    return len(self.name)

p = Person("Tim")
p * 4
print(p)
#=> My Person(^*Tim**Tim**Tim**Tim*^)

p(22)
#=> called this function 22
psn = Person("four") # there are four items in the string "four"
print(len(psn))      # #=> 4

# and now for something slightly different
from queue import Queue
import inspect

q1 = Queue()
print(q1) # this just returns an object address
#=> <queue.Queue object at 0x7fbb5ddaf240>

# OK let's now let's set things up so that when we print the queue by calling the
# print method on the declaration (q1 above, q2 below) we get s.thing meaningful
# to print in the console

print(inspect.getsource(Queue))
# <queue.Queue object at 0x7fd87ebac240>
# class Queue:
#     '''Create a queue object with a given maximum size.
#
#     If maxsize is <= 0, the queue size is infinite.
#     '''
# etc...this goes on forever

from queue import Queue as q
import inspect

class Queue(q):
  def __repr__(self):
    return f"Queue size is: ({self._qsize()})" #_qsize

  def __add__(self, item):
    self.put(item)

  def __sub__(self, item):
    self.get()

q2 = Queue() # <-------------- this is an empty queue

# without the "__add__" method above, this would generate an error:
# TypeError: unsupported operand type(s) for +: 'Queue' and 'int'
q2 + "a"
q2 + 8
q2 + True
q2 - [2, 3, 1, 0, 4]
print(q2)
#=> Queue size is: (3)
# this queue size is '3' because the queue just had 3 items .put() into it

print(list(q2.queue))
#=> [8, True]
