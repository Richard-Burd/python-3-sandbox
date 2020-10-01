# https://www.youtube.com/watch?v=IEEhzQoKtQU
# Python Threading Tutorial: Run Code Concurrently Using the Threading Module

# Later on, we are going to run code concurrently using the threading module
# but first, let's run some code synchronously, a graphic of this process is here:
# https://i.imgur.com/H4p2Tzc.jpg
import time

start = time.perf_counter()

def do_something():
  print('Sleeping 1 second...')
  time.sleep(1)
  print('Done Sleeping...')

# We're gonna run this function twice
do_something()
do_something()

finish = time.perf_counter()

print(f'Finished synchronous processes in {round(finish-start, 2)} second(s)')

# Now we are going to run code concurrently using threading, a graphic of this process is here:
# https://i.imgur.com/RIAmgiS.jpg
import threading

t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

start2 = time.perf_counter()

t1.start()
t2.start()

# https://stackoverflow.com/questions/15085348/what-is-the-use-of-join-in-python-threading
t1.join() # without this, the print statement below will execute before the function finishes running
t2.join() # without this, the print statement below will execute before the function finishes running

# the code below will only execute when the processes running above on t1 & t2 have finished

finish2 = time.perf_counter()

print(f'Finished concurrent processes using threading in {round(finish2-start2, 2)} second(s)')
