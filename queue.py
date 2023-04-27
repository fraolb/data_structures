#using deque
from collections import  deque
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)

queue.popleft()
print(queue)

#using list / array
'''
queue =[]
queue.append(1)
queue.append(2)
queue.append(3)

print(queue)

queue.pop(0)
queue.pop(0)
queue.pop(0)

print(queue)
'''