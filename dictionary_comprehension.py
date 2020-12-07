dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Double each value in the dictionary
double_dict = {k:v*2 for (k,v) in dict1.items()}

# Double each value in the dictionary only if the value is an even number
double_dict_if_even = {k:v*2 for (k,v) in dict1.items() if v%2 == 0}

# Identify odd and even entries
dict1_tripleCond = {k:('even' if v%2==0 else 'odd') for (k,v) in dict1.items()}

print(double_dict)
#=> {'a': 2, 'b': 4, 'c': 6, 'd': 8, 'e': 10}

print(double_dict_if_even)
#=> {'b': 4, 'd': 8}

print(dict1_tripleCond)

# Similarly, dictionaries can be nested and thus their comprehensions can be nested as well. Let's see what this means:
nested_dict = {'first':{'a':1}, 'second':{'b':2}}
float_dict = {
  outer_k: {float(inner_v) for (inner_k, inner_v) in outer_v.items()}
    for (outer_k, outer_v) in nested_dict.items()
}
print(float_dict)
#=> {'first': {1.0}, 'second': {2.0}}

people_dictionary = {'member_01':{'age':20, 'name':"Sal"}, 'member_02':{'age':23, 'name':"Tom"}}
people_names = {
  outer_k: {(inner_v)
    for (inner_k, inner_v) in outer_v.items() if inner_k == 'name' }
      for (outer_k, outer_v) in people_dictionary.items()
}

print(people_names)
#=> {'member_01': {'Sal'}, 'member_02': {'Tom'}}
