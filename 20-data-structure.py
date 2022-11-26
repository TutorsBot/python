# List as Stacks
# stacks = [23, 34, 44]
# stacks.append(22)
# stacks.append(55)
# print(stacks)


# stacks.pop()
# print(stacks)
# stacks.pop()
# print(stacks)


#List as Queues
from collections import deque
queue = deque([22, 34, 44])
# queue.appendleft(22)
# queue.appendleft(55)
# print(queue)

# queue.popleft()
# print(queue)
# queue.popleft()
# print(queue)

queue.extendleft([77, 88, 99])
print(queue)

queue.popleft()
