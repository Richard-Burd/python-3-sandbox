# Lesson 14 - Dictionaries
# https://www.youtube.com/watch?v=Gqby4v5JOu4&list=PL4cUxeGkcC9idu6GZ8EU_5B6WpKTdYZbK&index=14

# Dictionaries are the same as Javascript objects or Ruby hashes.
people_ages = {'ron':12, 'bob':5, 'tom':36, 'dan':41, 'cat':39, 'alf':73}

print(people_ages)

# check to see if a key exists inside the dictionary
print('ron' in people_ages)

# find the value for the key in the dictionary
print(people_ages['ron'])

# get the keys for the dictionary
print(people_ages.keys())

# get the same thing returned as an actual list (i.e. "array" in Ruby or JS)
print(list(people_ages.keys()))

# get the values back as a list (i.e. "array" in Ruby or JS)
print(list(people_ages.values()))

my_names = list(people_ages.keys())

print("there's ", my_names.count('ron'), "ron in the list!")

# this is a different way to declare a dictionary
person = dict(name='shaun', age=27, height=6)

# When called, the syntax has ":" instead of "=" and the keys are in quotations 'name'
print(person) #=> {'name': 'shaun', 'age': 27, 'height': 6}

ninja_belts = {}

while True:
  ninja_name = input('enter a ninja name:')
  ninja_belt = input('enter a belt color:')

  # grab the key (in the dictionary) you just defined above and give it a value
  # you assigned right below it
  ninja_belts[ninja_name] = ninja_belt

  another = input('add another? (y/n)')
  if another == 'y':
    continue
  else:
    break

print(ninja_belts)

def ninja_intro(dictionary):
  # cycle through the dictionary
  for key, val in dictionary.items():
    print(f'I have a key of: {key} and a value of: {val} !')

ninja_intro(ninja_belts)
