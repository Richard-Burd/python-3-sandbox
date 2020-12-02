my_new_var = {}
print(type(my_new_var))
#=> <class 'dict'>

number_list = [1, 6, 3, 2, 4, 4, 1, 0, 7, 2]
print(sorted(number_list))
#=> [0, 1, 1, 2, 2, 3, 4, 4, 6, 7]

number_set = {1, 6, 3, 2, 4, 4, 1, 0, 7, 2}
print(sorted(number_set))
#=> [0, 1, 2, 3, 4, 6, 7]

people_list = ['ron', 'Bob', 'Tom', 'Dan', 'cat', 'alf', 'ron']
print(sorted(people_list))
#=> ['Bob', 'Dan', 'Tom', 'alf', 'cat', 'ron', 'ron']

people_set = {'ron', 'Bob', 'Tom', 'Dan', 'cat', 'alf', 'ron'}
print(sorted(people_set))
#=> ['Bob', 'Dan', 'Tom', 'alf', 'cat', 'ron']

print(set(number_set))
#=> {0, 1, 2, 3, 4, 6, 7}

print(set(people_list))
#=> {'Tom', 'alf', 'ron', 'cat', 'Dan', 'Bob'}

# https://stackoverflow.com/questions/2831212/python-sets-vs-lists/2831242
# Lists are slightly faster than sets when you just want to iterate over the values.  Sets, however, are significantly faster than lists if you want to check if an item is contained within it. They can only contain unique items though. It turns out tuples perform in almost exactly the same way as lists, except for their immutability. -Ellis Percival

# It is possible to do comprehension on sets
my_set = {5, 'a', '3', 6, 'Q', 2}
print([elem for elem in my_set])
#=> [2, 5, 6, '3', 'Q', 'a']

# Sets are mutable
a_new_set = set("abcdef")
print(a_new_set)
#=> {'f', 'd', 'b', 'c', 'e', 'a'}
a_new_set.add("my string")
print(a_new_set)
#=> {'e', 'a', 'f', 'd', 'c', 'my string', 'b'}
#=> NOTE: the order above will change each time the code is ran because there is no true order to a set, unlike a list

# Elements of a set cannot be mutable objects
mutable_thing = [1, 2, 7]
a_new_set.add(mutable_thing)
#=> TypeError: unhashable type: 'list'
del a_new_set

# here we are typecasting the ages into a set using the set() method so that we do not have duplicate ages down here
people_ages = {'ron':7, 'bob':12, 'tom':12, 'dan':1, 'cat':1, 'alf':1}
print(set(people_ages.values()))
#=> {1, 12, 7}
set(people_ages.keys())
#=> {'alf', 'tom', 'cat', 'dan', 'ron', 'bob'}

 def age_count(dictionary):
   ages = list(dictionary.values())
   for age in set(ages):
     number = ages.count(age)
     print(f'There are {number} people aged {age}')

age_count(people_ages)
#=> There are 3 people aged 1
#=> There are 2 people aged 12
#=> There are 1 people aged 7
