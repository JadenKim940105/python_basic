class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(data)

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def delete(self, data):
        if self.head is None:
            print("해당 값을 가진 노드가 존재하지 않습니다")
        elif self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp # 객체 삭제
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                else:
                    node = node.next



linkedList1 = NodeMgmt(0)

for data in range(1, 10):
    linkedList1.add(data)

linkedList1.desc()

linkedList1.delete(4)

linkedList1.desc()
linkedList1.delete(9)
linkedList1.desc()