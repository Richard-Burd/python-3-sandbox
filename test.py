# This is a place to import Python files with a long directory just to see how that
# would work.

from lessons.space.planet import Planet

print(Planet)
#=> <class 'lessons.space.planet.Planet'>

from collections import Counter, deque, namedtuple, OrderedDict

a = Counter('gallad')
print(a)
#=> Counter({'a': 2, 'l': 2, 'g': 1, 'd': 1})

d = deque("hello")
print(d)
#=> deque(['h', 'e', 'l', 'l', 'o'])

Point = namedtuple('Point', 'x y z time')
newP = Point(3, 4, 5, '12:00pm')
print(newP)
#=> Point(x=3, y=4, z=5, time='12:00pm')
