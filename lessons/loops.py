# Lesson 9 - For Loops
# https://www.youtube.com/watch?v=ENMCxQ9kNS4&list=PL4cUxeGkcC9idu6GZ8EU_5B6WpKTdYZbK&index=9

ninjas = ['ryu', 'shu', 'snu', 'moe', 'bob', 'dua']

# start  with index 1 (shu)
# and go up to index  3 (moe) - but don't include index 3
for ninja in ninjas[1:3]:
  print(f'we have: {ninja}')
# => we have: shu
# => we have: snu

# a more complex loop
for ninja in ninjas:
  if ninja == 'moe':
    print(f'{ninja} - is the last ninja')
    break # after 'moe', break out of the loop and ignore the other elements
  else:
    print(ninja)
# => ryu
# => shu
# => snu
# => moe - is the last ninja

# Lesson 10 - While Loops
# https://www.youtube.com/watch?v=ENMCxQ9kNS4&list=PL4cUxeGkcC9idu6GZ8EU_5B6WpKTdYZbK&index=10

age = 25
num = 0

while num < age:
  if num == 4:
    print("That's number 4! OK, let's continue on...")
    num += 1
    continue # this will concinue on with the iteration after doing the stuff above
  if num % 2 == 0:# this will give us only even numbers
    print(num)    # <= Without this specific indentation, this will not work
  num += 1        # <= Without this specific indentation, this will not work
