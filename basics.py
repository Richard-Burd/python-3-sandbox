# Lesson 3 - Numbers
# https://www.youtube.com/watch?v=Gqby4v5JOu4&list=PL4cUxeGkcC9idu6GZ8EU_5B6WpKTdYZbK&index=3

# everything in Python is an object, and objects have attributes & methods that are functions

type(500)
# <class 'int'>
type(5.1)
# <class 'float'>

5 / 5
# 1.0 <= retruns a float

5 / 5
# 1   <= retruns an integer

10 % 3
# 1 <= remainder, or 'modulus'

5 ** 5
# 3125 <= 5 to the power of 5

5 + 5 * 3
# 20

(5 + 5) * 3
# 30

# (BIDMAS) Brackets -> Indices -> Multiplication -> Addition -> Subtraction
age = 25
age += 5 # or -= for the opposite
age
# 35
wages = 1000
bills = 200
rent = 500
food = 200
savings = wages - bills - rent - food
savings
# 100

# Lesson 4 - Strings
# https://www.youtube.com/watch?v=Gqby4v5JOu4&list=PL4cUxeGkcC9idu6GZ8EU_5B6WpKTdYZbK&index=4

noun = 'you\'re here' # canceler

greet = 'hello'
greet[0:4]
# 'hell'

greet[2:-1]
# 'll'

greet + " " + noun
# hello you're here

greet * 3
# 'hellohellohello'

greet.upper()
# Hello

len(greet)
# 5

cheeses = "Brie, Chedder, Stilton"
cheeses.split(',')
# ['Brie', 'Chedder', 'Stilton']

# Lesson 5 - Lists
# https://www.youtube.com/watch?v=Gqby4v5JOu4&list=PL4cUxeGkcC9idu6GZ8EU_5B6WpKTdYZbK&index=5

list1 = ['Bob', 'Tom', 'Ron'] # Ruby or JavaScript "array"
list1[1]
# 'Tom'

list2 = list1 + ["Cat"]
# ['Bob', 'Tom', 'Ron', 'Cat']

list2.append('Dan')
# ['Bob', 'Tom', 'Ron', 'Cat', 'Dan']

list2.pop() # removes the last item ('Dan')
# ['Bob', 'Tom', 'Ron', 'Cat']

list2.remove('Tom')
# ['Bob', 'Ron', 'Cat']

del(list2[0])
# ['Ron', 'Cat']

nest = [[1, 2], [3, 4], [5, 6]]

nest[2][1]
# 6


print()
