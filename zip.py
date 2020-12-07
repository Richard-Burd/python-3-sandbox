# Python zip() Function
# https://www.w3schools.com/python/ref_func_zip.asp

# The zip() function returns a zip object, which is an iterator of tuples where
# the first item in each passed iterator is paired together, and then the second
# item in each passed iterator are paired together etc.  If the passed iterators
# have different lengths, the iterator with the least items decides the length
# of the new iterator.

names = ("John", "Charles", "Mike")
ages = (25, 22, 34, 57)

output = zip(names, ages)

# use the tuple() or dict() functions to display a readable version of the result:
print(tuple(output))
#=> (('John', 25), ('Charles', 22), ('Mike', 34))

# You cannot do both!
# print(dict(output))
#=> {'John': 25, 'Charles': 22, 'Mike': 34}
