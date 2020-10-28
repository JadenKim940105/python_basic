queue = list()

def enque(data):
    queue.append(data)

def deque():
    data = queue[0]
    del queue[0]
    return data

enque(5)
enque(6)
enque(7)

print(deque())

enque(8)

print(deque())
print(deque())
print(deque())
