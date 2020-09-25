# https://www.youtube.com/watch?v=jmx1OZNMLr0&list=PLzMcBGfZo4-mFu00qxl0a67RhjjZj3jXm&index=9
# Python Programming Tutorial #9 - Iteration by Item (For Loops Continued...)

fruits = ["apple", "pears", "peach", "berry"]

# iterating by item
for fruit in fruits:
  print(fruit[0:3]) # grab elements 0 to 3 in each list item

#iterating by index
for x in range(1,5):
  print(x)

# This is a standard for loop you would use:
for fruit in fruits:
  if fruit == 'pears':
    print('found some pears!')
  else:
    print('no pears')

# You can use a range but it's suboptimal:
for x in range(0, 3): # We're only going to [3] in the list
  if fruits[x] == 'peach':
    print('found some canned peaches :)')
  else:
    print('no canned peaches :(')

# Here we'll define the length of the list so we iterate over all its items
for x in range(len(fruits)): # len(fruits) gives a value of 4 cuz there's 4 items in "fruits" above
  if fruits[x] == 'apple':
    print('found some apples :)')
  else:
    print('no apples :(')

# Cool notes:
# https://www.geeksforgeeks.org/python-get-first-element-of-each-sublist/
