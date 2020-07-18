age = int(input('Enter your age:'))

if age < 10:
  # Python expects the code block to be intented
  print('you are under 10')
elif age >= 10 and age <= 20: # && = and in python
  print('You\'re a teenager ')
elif age == 33:
  print("You're middle aged")
else:
  print("That is old")
