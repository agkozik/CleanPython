from collections import deque
q = deque()
q.append('One')
q.append('Two')
q.append('Three')

print(q)

for i in q:
    print(i)

print(q.popleft())
print(q.popleft())
print(q.popleft())
print(q.popleft())


