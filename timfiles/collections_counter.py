# https://www.youtube.com/watch?v=cgDRugJzBfM&list=PLzMcBGfZo4-nhWva-6OVh1yKWHBs4o_tv&index=6
# Intermediate Python Tutorial #6 - Collections /Counter()

# import collections
from collections import Counter

# Python Containers:
  # list
  # set
  # dictionary (dict)
  # tuple - immutable

# These are Python Data Types introduced by the Collections Module
# (from collections import...etc):
# You have to import them to use them
  # 1.) counter <- This lesson
  # 2.) deque
  # 3.) namedTuple()
  # 4.) orderedDict
  # 5.) defaultDict

a = Counter('gallad')
print(a)
#=> Counter({'a': 2, 'l': 2, 'g': 1, 'd': 1})

a = Counter(['a', 'a', 'b', 'c', 'c'])
print(a)
#=> Counter({'a': 2, 'c': 2, 'b': 1})

a = Counter({'a':1, 'b':2})
print(a)
#=> Counter({'b': 2, 'a': 1})

a = Counter(cats=4, dogs=7) #keys can't be mixed
print(a['cats'])
#=> 4

print(a['lizards']) # this will return 0 instead of an error
#=> 0

print(list(a.elements()))
#=> ['cats', 'cats', 'cats', 'cats', 'dogs', 'dogs', 'dogs', 'dogs', 'dogs', 'dogs', 'dogs']

b = Counter({'x':2, 'y':7, 34:8, 3:1, 'z':45}) # keys can have mixed data types
print(list(b.elements()))
#=> ['x', 'x', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 34, 34, 34, 34, 34, 34, 34, 34, 3, 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z']

# Two most common pairs are shown because of this -------------2 below
print(f'The two most common key-value pairs are {b.most_common(2)}')
#=> The two most common key-value pairs are [('z', 45), (34, 8)]

b.subtract('z') # you can subtract any of the strings but not integers (e.g. 34 or 3)
print(b)
#=> Counter({'z': 44, 34: 8, 'y': 7, 'x': 2, 3: 1})
#                                         |
d = ['x', 'x', 'x', 'x'] #                |
b.update(d) #                             |
print(b) #                                |
#=> Counter({'z': 44, 34: 8, 'y': 7, 'x': 6, 3: 1})
# this just added four 'x's to the counter named: b
b.clear() # This will clear the counter of all its contents
print(b)
#=> Counter()

# Intersection & Union of Counters
a = Counter({'x':1, 'y':2, 'z':3})
b = Counter({'x':10, 'y':10, 'z':10})

print(a+b)
#=> Counter({'z': 13, 'y': 12, 'x': 11})
