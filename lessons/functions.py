# Lesson 12 - Functions
# https://www.youtube.com/watch?v=Gqby4v5JOu4&list=PL4cUxeGkcC9idu6GZ8EU_5B6WpKTdYZbK&index=12

# starts with "def" and ends with nothing at all (i.e. no "end" like in Ruby or JS)
# default parameters like Ruby & JS
def greet(name = "Moe", time = "Zulu"): # use colon ":" like w/ loops & ranges
  print(f"Hey {name} it's {time} right now!")

# name = input('enter your time:')
# time = input('enter the time:')
# greet(name, time)


# pi
def area(radius):
  return 3.142 * radius * radius

def volume(area, length):
  print(area * length)

radius = int(input('enter a radius:'))
length = int(input('enter a length'))

# pass a function into another function
volume(area(radius), length)
