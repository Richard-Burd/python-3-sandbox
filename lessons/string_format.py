num1 = 3.1425
num2 = 10.2903

# Format Method
#                             0 in the array =>         1 in the array=> array=[num1,num2]
print('The first variable is {0} and the second one is {1}'.format(num1, num2))

# Only show 3 digits             3                            3
print('The first variable is {0:.3} and the second one is {1:.3}'.format(num1, num2))

# Using "F-Strings"
#    "f"                            "2" <------decemal places------> "1"
print(f'The first variable is {num1:.2f} and the second one is {num2:.1f}')
