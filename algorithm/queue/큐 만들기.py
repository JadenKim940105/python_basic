import queue

data_queue = queue.Queue()

data_queue.put("funcoding")
data_queue.put(1)


for i in range(data_queue.qsize()):
    print(data_queue.get(i))


data_queue.put(3)
print(data_queue.get())
print(data_queue.get())
print(data_queue.qsize())

