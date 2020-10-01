# https://www.youtube.com/watch?v=IEEhzQoKtQU
# Python Threading Tutorial: Run Code Concurrently Using the Threading Module

# we are going to run code concurrently using the threading module
# but first, let's run some code synchronously
import time

start = time.perf_counter()

def do_something():
  print('Sleeping 1 second...')
  time.sleep(1)
  print('Done Sleeping...')

do_something()
do_something()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
