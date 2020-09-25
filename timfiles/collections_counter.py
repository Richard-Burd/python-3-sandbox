# https://www.youtube.com/watch?v=cgDRugJzBfM&list=PLzMcBGfZo4-nhWva-6OVh1yKWHBs4o_tv&index=6
# Intermediate Python Tutorial #6 - Collections /Counter()

import collections
from collections import Counter

# Python Containers:
  # list
  # set
  # dictionary (dict)
  # tuple - immutable

# Python Data Types
  # 1.) counter <- This lesson
  # 2.) deque
  # 3.) namedTuple()
  # 4.) orderedDict
  # 5.) defaultDict

a = Counter('gallad')
print(a)
a = Counter(['a', 'a', 'b', 'c', 'c'])
print(a)
a = Counter({'a':1, 'b':2})
print(a)
a = Counter(cats=4, dogs=7) #keys can't be mixed
print(a['cats'])
print(a['lizards']) # this will return 0 instead of an error
print(list(a.elements()))
b = Counter({'x':2, 'y':7, 34:8, 3:1, 'z':45}) # keys can have mixed data types
print(list(b.elements()))

# Two most common pairs are shown because of this -------------2 below
print(f'The two most common key-value pairs are {b.most_common(2)}')
