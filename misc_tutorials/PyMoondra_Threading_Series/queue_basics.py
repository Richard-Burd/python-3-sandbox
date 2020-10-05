# NOTE: This video is part 6 of an 11 part advanced tutorial series on threading.
# The code below only deals with queues and not threading.

# https://www.youtube.com/watch?v=bnm5_GH04fM
# Python Tutorials : Threading Beginners Tutorial- Queue (part 6-1)

# Queues are containers of data items / commands that are waiting to be retrieved
# You can control the flow of your tasks utilizing queues

# 3 types of queues are FIFO, LIFO, and Priority

# FIFO (First-in-first-out)

# LIFO (Last-in-first-out)

# Priority

import queue
# this is a FIFO queue, which is the default queue type
q = queue.Queue()

q.put(5) # this is the first item in, and the first item out (FIFO)
q.put(1)
q.put("three")
q.put("7")

# .get() will return 5 because the 5 was the first item put into the queue and
# so it will be the first one out since this default queue is a FIFO
print(q.get())
#=> 5

print(q.get())
#=> 1

# There are still two more items in the queue (the 1 and the "7")
print(q.empty())
#=> False

print("\n")
print("FIFO Queue:")

# Let's view the remaining items in the queue:
# we use .empty() instead of .get() because the latter will cause our computer
# to lock up when there are no more items to actually ".get()" in the queue
# to solve that problem we will use threading below, but for now let's use ".empty()"
while not q.empty():
  print(q.get(), end = ' ^ ')
#=> 1 ^ 7 ^

# This will lock up without using threading:
# print('first item gotten')
# print(q.get())
# print('finished')

# Left off doing this on 9:34 / 12:53 of https://www.youtube.com/watch?v=bnm5_GH04fM
# Author reccomends doing the entire tutorial before advancing:
# https://www.youtube.com/playlist?list=PLGKQkV4guDKEv1DoK4LYdo2ZPLo6cyLbm

# import threading
# import time
#
# def putting_thread(q):
#   while True:
#     print('starting thread')
#     time.sleep(10)
#     q.put(5)
#     print('put s.thing in the queue')

# q2 = queue.Queue()
# t1 = threading.Thread(target = putting_thread, args = (q2,),deamon) = True

print("\n")
print("LIFO Queue:")

# https://www.youtube.com/watch?v=wkPMom77Hqk
# Python Tutorials : Threading Beginners Tutorial- Queue - part 6-2
# LIFO (Last In First Out) Queue
# It's the same process as above, but we add "Lifo" to the Queue:
q2 = queue.LifoQueue()

q2.put("Ron")
q2.put("Tom")
q2.put("Dan") # this is the last item in, and the first item out (LIFO)

while not q2.empty():
  print(q2.get(), end = ' ^ ')
#=> Dan ^ Tom ^ Ron ^

print("\n")
print("Priority Queue:")

# Priority Queue
# The item with the lowest value is (by default) out first
import time

q3 = queue.PriorityQueue()

q3.put(1)
q3.put(3)
q3.put(4)
q3.put(2)

# here's an example to show how priority queue works; the lowest values are
# listed first...but what if you have strings instead of integers!? for that
# you'll need tuples
for i in range(q3.qsize()):
  print(q3.get())
#=> 1
#=> 2
#=> 3
#=> 4

print("\n")
print("Priority Queue using Tuples:")

q4 = queue.PriorityQueue()

q4.put((1, 'Priority 1'))
q4.put((3, 'Priority 3'))
q4.put((4, 'Priority 4'))
q4.put((2, 'Priority 2'))

for i in range(q4.qsize()):
  print(q4.get())
#=> (1, 'Priority 1')
#=> (2, 'Priority 2')
#=> (3, 'Priority 3')
#=> (4, 'Priority 4')
