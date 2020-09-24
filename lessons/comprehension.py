# let's say we have a list of prizes and we want to double each one
prizes = [5, 10, 50, 100, 1000]
double_prizes = [] # create an empty array

for prize in prizes:
  double_prizes.append(prize*2)

print(double_prizes)

# comprehension method: this gives the same values as above but is much shorter
double_prizes = [prize*2 for prize in prizes]
print(double_prizes)

# squaring of even numbers from 1 to 10.
nums = [1,2,3,4,5,6,7,8,9,10]
squared_even_numbers = []

# Let's see another example of how to use comprehension

for num in nums:
  # if the number squared modulus 2 (if the number is even)
  if(num**2) % 2 == 0:
    squared_even_numbers.append(num**2)
print(squared_even_numbers)

# another use of the comprehension method:
squared_even_numbers = [
  num**2 for num in nums if(num**2) % 2 == 0
]
print(squared_even_numbers)
