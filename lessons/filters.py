grades = ['A', 'B', 'F', 'C', 'F', 'D', 'A']

# Want to get rid of the bad grades in my list...
# this is the format for the 'filter()' method:
# filter(testing_function, list)

# testing function needs to be setup first:
def remove_bad_grades(my_grade):
  return my_grade != 'F' and my_grade != 'D'

print(filter(remove_bad_grades, grades))
#=> <filter object at 0x7f0aaf84b780>

# now we need to typecast the result to make it readable:
print(list(filter(remove_bad_grades, grades)))
#=> ['A', 'B', 'C', 'A']



# here's how to do the same thing using a for loop, it's a bit longer:
filtered_grades = []
for grade in grades:
  if grade != 'F' and grade != 'D':
    filtered_grades.append(grade)
print(filtered_grades)


# Let's use comprehension, it's the shortest way:
print([grade for grade in grades if grade != 'F' and grade != 'D'])
