# https://www.youtube.com/watch?v=GKgpvriuQY8&list=PLzMcBGfZo4-nhWva-6OVh1yKWHBs4o_tv&index=7
# Intermediate Python Tutorial #7 - Collections/namedtuple()

print("named tuple")

# import collections
from collections import namedtuple

# Python Containers:
  # list
  # set
  # dictionary (dict)
  # tuple - immutable

# These are Python Data Types introduced by the Collections Module
# (from collections import...etc):
# You have to import them to use them
  # 1.) counter
  # 2.) deque
  # 3.) namedTuple()  <- This lesson
  # 4.) orderedDict
  # 5.) defaultDict

# The main difference between a regular tuple and a named tuple is that you can
# access things by element and it's a lot nicer to read in your program

# the first variable is Capitalized like a class name, and is the name of the tuple,
# the second variable is a string with all the element names
Point = namedtuple('Point', 'x y z time')

newP = Point(3, 4, 5, '12:00pm')
print(newP)
#=> Point(x=3, y=4, z=5, time='12:00pm')

# You don't have to, but you can embed the elements in "[]" like so:
Coor = namedtuple('Coordinates', ['lat', 'lon'])
new_coor = Coor(20.213, 499.340)
print(new_coor)
#=> Coordinates(lat=20.213, lon=499.34)

# You can even do this with dictionaries like so:
# start out with generic "0" values just to populate the dictionary:
Data = namedtuple('Data_Set', {'x':0, 'y':0, 'z':0})
new_data = Data(10, 20, 30)
print(new_data)
#=> Data_Set(x=10, y=20, z=30)

# Namedtuples allow for the use of dot notation, regular tuples do not:
print(new_data.x)
#=> 10

# we can also find elements by index
print(new_data[0])
#=> 10

# we can also get the values returned to us as a dictionary:
print(new_data._asdict())
#=> OrderedDict([('x', 10), ('y', 20), ('z', 30)])

# we can print out the keys:
print(new_data._fields)
#=> ('x', 'y', 'z')

# we can replace the value of a specified key, but this is not destructive,
# in other words, we need to assign a new value to the operation because we
# cannot change the original namedtuple in this way.

# first, define the new value:
my_new_value = new_data._replace(y=88)
print(my_new_value)
#=> Data_Set(x=10, y=88, z=30)

# I can use the Make method to create a new instance of the Data class but
# this new instance will have different values in the list:
p2 = Data._make(['a', 'b', 'c'])
print(p2)
#=> Data_Set(x='a', y='b', z='c')

# NOTE: these are now strings, not integers as in the original declaration above
