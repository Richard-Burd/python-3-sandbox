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

q.put(5)
q.put(1)
q.put("7")

# .get() will return 5 because the 5 was the first item put into the queue and
# so it will be the first one out since this default queue is a FIFO
print(q.get())
#=> 5

# There are still two more items in the queue (the 1 and the "7")
print(q.empty())
#=> False

# Let's view the remaining items in the queue:
while not q.empty():
  print(q.get(), end = ' ^ ')
#=> 1 ^ 7 ^
