# https://www.youtube.com/watch?v=m3JgSV1Obn8&list=PLzMcBGfZo4-nhWva-6OVh1yKWHBs4o_tv&index=8
# Intermediate Python Tutorial #8 - Collections/Deque(deck)

from collections import deque # pronounced like "deck"

# Python Containers:
  # list
  # set
  # dictionary (dict)
  # tuple - immutable

# These are Python Data Types introduced by the Collections Module
# (from collections import...etc):
# You have to import them to use them
  # 1.) counter
  # 2.) deque              <- This lesson
  # 3.) namedTuple()
  # 4.) orderedDict
  # 5.) defaultDict

# Why use a deque over a traditional list?  because it's faster in terms of adding
# items to the beginning and end of the list...but if you're going to want to
# randomally access elements within the container, it's better to use a
# traditional list.

d = deque("hello")
print(d)
#=> deque(['h', 'e', 'l', 'l', 'o'])

d.append('4')
d.append('5')
d.appendleft('2')
d.appendleft(1)
d.appendleft(True)
print(d)
#=> deque([True, 1, '2', 'h', 'e', 'l', 'l', 'o', '4', '5'])

# I can destructively remove elements from the front or back of the deque:
d.pop() # defaults to index [0]
d.popleft() # defaults to index [0]
print(d)
#=> deque([1, '2', 'h', 'e', 'l', 'l', 'o', '4'])

# This will remove everything from the deqe
d.clear()
print(d)
#=> deque([])

# extend() takes in anything iterable, such as a list or string, ant puts it at
# the end of our list.
d.extend('456')
d.extend('hello')
d.extendleft('123') # this one reverses the order
print(d)
#=> deque(['3', '2', '1', '4', '5', '6', 'h', 'e', 'l', 'l', 'o'])

# The rotate() method shifts the order of items as shown below:
x = deque("123456")
print(x)
#=> deque(['1', '2', '3', '4', '5', '6'])

x.rotate(-1)
print(x)
#=> deque(['2', '3', '4', '5', '6', '1'])

x.rotate(2)
print(x)
#=> deque(['6', '1', '2', '3', '4', '5'])

# the maxlen method limits the number of items in the deque:
w = deque("Interlochen", maxlen=5)
print(w)
#=> deque(['o', 'c', 'h', 'e', 'n'], maxlen=5)
print(w.maxlen)
#=> 5

# NOTE: you cannot reassign this 'maxlen' value after it's initially declared

# ...you can only add to the deque with the extend method, but that will still
# mantain the originam maxlen of 5
w.extend([1, 2, 3])
print(w)
#=> deque(['e', 'n', 1, 2, 3], maxlen=5)
