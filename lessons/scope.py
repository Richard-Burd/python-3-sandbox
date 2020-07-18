# Lesson 13 - Scope
# https://www.youtube.com/watch?v=Gqby4v5JOu4&list=PL4cUxeGkcC9idu6GZ8EU_5B6WpKTdYZbK&index=13

# my_name is global and is accessable inside the function
my_name = 'Abe'

def first_level():
  # my_name is global and is accessable inside the function
  print(my_name, 'is global but seen in the first_level() function')

  # another_name is scoped to the function and is not global
  another_name = 'Tod'
  print(another_name, 'is scoped here in the first_level() function')

  def second_level():
    print(another_name, 'is in second_level() but scoped to the first_level() function')

  # call the second_level() function inside the first_level() function.
  second_level()

first_level()
