# Lesson 11 - Ranges
# https://www.youtube.com/watch?v=ENMCxQ9kNS4&list=PL4cUxeGkcC9idu6GZ8EU_5B6WpKTdYZbK&index=11

# go from 0, up to but not incuding 5
for n in range(5):
  print(n)

# go from and include 5, up to but not incuding 10
for n in range(5,10):
  print(n)

# go from and include 10, up to but not incuding 1000, in intervals of 200
for n in range(10,1000, 200):
  print(n)

names = ['ron', 'bob', 'tom', 'dan', 'cat', 'alf']

for n in range(len(names)):
  # [n] represents each element
  print(n + 1, ".)", names[n].capitalize())

print("Now let's go backwards...")
#                         -1            the start position is the last "-" item in the array
#                             -1        the end position is the last "-" item in the order
#                                 -1    the increment ammt. going backwards "-"
for n in range(len(names) -1, -1, -2):
  print(n + 1, ".)", names[n])
