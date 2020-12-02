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
