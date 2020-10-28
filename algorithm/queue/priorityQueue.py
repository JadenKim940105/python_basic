import queue

dataQueue = queue.PriorityQueue()

dataQueue.put((1, 'korea'))
dataQueue.put((10, 'america'))
dataQueue.put((5, 'canada'))

print(dataQueue.get())
print(dataQueue.get())

queue_list = list()

def enqueue(data):
    queue_list.append(data)

def dequeue(data):
    data = queue_list[0]
    del queue_list[0]
    return data

for index in range(10):
    enqueue(index)

for i in range(len(queue_list)):
    print(dequeue(i))


