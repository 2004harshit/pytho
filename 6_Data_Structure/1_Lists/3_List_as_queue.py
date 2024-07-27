from collections import deque

queue = deque(['DBMS','Soft Skills','TOC','MEFA','MATHS'])

print(queue , "  Type  = ",type(queue))

queue.append(100)

print(queue)

queue.appendleft("HELLO")

print(queue)

queue.popleft()

print(queue)
