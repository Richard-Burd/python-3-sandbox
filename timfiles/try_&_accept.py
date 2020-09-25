# https://www.youtube.com/watch?v=MImAiZIzzd4&list=PLzMcBGfZo4-mFu00qxl0a67RhjjZj3jXm&index=18
# Python Programming Tutorial #18 - Try and Except (Python Error Handling)

print("Enter a username that consists only of numbers")
text = input("Username: ")

# Try & accept lets you run code that actually would crash if it is falsey
# Here I want my string to only be numbers
try:
  number = int(text) # typecast the text into an integer
  print(f'So, {number} is in fact a legit username!')
except: # what happens of the "try:" block of code doesn't run & crashes instead
  print("Invalid username, access denied :(")
