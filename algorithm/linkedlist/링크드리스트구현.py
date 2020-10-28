class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        dummy = Node("dummy")
        self.head = dummy
        self.tail = dummy

        self.current = None
        self.before = None

        self.num_of_data = 0

    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node

        self.num_of_data += 1
