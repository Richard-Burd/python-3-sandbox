# Lambdas are a bit like anonymous functions in JavaScript
# They're used for functions we're only gonna use once

# let's start with a list
nums = [1, 2, 3, 4, 5, 6]

# let's create a simple function to do s.thing (i.e. square a number)
def square(n):
  return n*n

# Normally this is how we would go through and square each element in the list:
# list(map(some_function, list))
print(list(map(square, nums))) #=> [1, 4, 9, 16, 25, 36]



# Since we're only calling this "square()" function once, we could use a lambda:
lambda n: n*n #=> It's automatically gonna return the result on the right of ":"
# there is no need to state "return" in here, just drop the lambda into place:
print(list(map(lambda n: n*n, nums))) #=> [1, 4, 9, 16, 25, 36]

# You could pass in multiple arguments into a lambda like this:
# lambda x, y, z: n*n
