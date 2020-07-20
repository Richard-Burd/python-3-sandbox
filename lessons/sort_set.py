# sorted() method sorts numbers & strings:
numbers = [1, 6, 3, 2, 4, 4, 1, 0, 7, 2]
print(sorted(numbers))
#=> [0, 1, 1, 2, 2, 3, 4, 4, 6, 7]

# sorted() method lists the names with capital letters first:
people = ['ron', 'Bob', 'Tom', 'Dan', 'cat', 'alf', 'ron']
print(sorted(people))
#=> ['Bob', 'Dan', 'Tom', 'alf', 'cat', 'ron', 'ron']

# set() method takes out all the duplicates, but returns a dictionary, not a list.
print(set(numbers))
#=> {0, 1, 2, 3, 4, 6, 7}

# set() will remove duplicates in a list of strings, but it will not order them
print(set(people))
#=> {'Tom', 'alf', 'ron', 'cat', 'Dan', 'Bob'}

# set() will remove duplicates in a dictionary, but it will not order them
people_ages = {'ron':7, 'bob':12, 'tom':12, 'dan':1, 'cat':1, 'alf':1}
print(set(people_ages.values()))
#=> {1, 12, 7}

def age_count(dictionary):
  ages = list(dictionary.values())
  for age in set(ages):
    number = ages.count(age)
    print(f'Ther are {number} different ages')

age_count(people_ages)
