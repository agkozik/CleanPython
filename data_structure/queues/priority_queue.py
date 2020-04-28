from queue import PriorityQueue


q = PriorityQueue()
q.put((2, 'Two'))
q.put((1, 'One'))
q.put((3, 'Three'))

while not q.empty():
    next_item = q.get()
    print(next_item)
