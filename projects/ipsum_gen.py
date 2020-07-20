# Lesson 28
# https://www.youtube.com/watch?v=iLS4Hk-kJXE&list=PL4cUxeGkcC9idu6GZ8EU_5B6WpKTdYZbK&index=28
from random import randint

# we will take these ninja works and randomly inject them into the loreum ipsum text
ninja_words = [
  'Aiki', 'Buyu', 'Chimonjutsu', 'Cho sen', 'Dojo', 'Gakusei', 'Haiboku',
  'Jin', 'Kenshi', 'Obake ken', 'Rakusha', 'Sanmaru', 'Tekkon', 'Yoko'
]

# this takes in a wor each time we are looping
def ninjarize(word):
  random_pos = randint(0, len(ninja_words) - 1)
  return f'{word} {ninja_words[random_pos]}'

# this will use the "input()" method to get an ansewr from the user in bash
paragraphs = int(input('How many paragraphs of ninja ipsum: '))

# grabbing the .txt file external to this script:
with open('ipsum.txt') as ipsum_original:

  # ".read()"  will read the file
  # ".split()" will take each work and make it an element in a list called "items"
  items = ipsum_original.read().split()

  # now we need to loop through each paragraph
  for n in range(paragraphs): # this is an integer from the user
    ninja_text = list(map(ninjarize, items) )
    with open('ninja_ipsum.txt', 'a') as ipsum_ninja:
      ipsum_ninja.write(' '.join(ninja_text) + '\n\n')
