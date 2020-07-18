# Lesson 6 - Standard Input
# https://www.youtube.com/watch?v=Gqby4v5JOu4&list=PL4cUxeGkcC9idu6GZ8EU_5B6WpKTdYZbK&index=6

# take in user input & print their output (type ctrl + / to comment out multiple blocks)
# name = input("What's your name?")
# age = input("...and what's your age?")
# print('Hi there ' + name + " you are", age)

# Calculate the area of a circle:
radius = input("Enter the radius of your circle (m):")

# User inputs are always a string...
# Their numbers must be type-casted with "int()" to become integers
area = 3.142 * int(radius) ** 2
print('The area of your circle is:', int(area))
