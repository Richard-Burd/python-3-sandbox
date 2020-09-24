# we need the random module from the Python Standard Library:
# https://docs.python.org/3/library/
from random import shuffle

words = ['ron', 'cat', 'pat']

anagrams = []

def jumble(word):
  anagram = list(word) # ['r', 'o', 'n']
  shuffle(anagram)
  return ''.join(anagram)

for word in words:                                           # long form
  anagrams.append(jumble(word))                              # long form
print(anagrams) #=> ['orn', 'cta', 'atp']

# map(function, data)
print(map(jumble, words)) #=> <map object at 0x7faa43897128>

# Now let's typecast the object to see the list:
print(list(map(jumble, words))) #=> ['nor', 'tca', 'tap']    # short form

# Now let's use a comprehension:
print([jumble(word) for word in words])                      # another short form
