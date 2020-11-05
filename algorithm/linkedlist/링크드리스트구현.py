class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


node1 = Node(1)
node2 = Node(2)
node1.next = node2
head = node1

def add(data):
    node = head
    while node.next:
        # node.next 에 다음 Node 정보가 담겨있다면
        node = node.next # 다음 node 로 이동
        # node.next 에 다음 Node 정보가 없다면
    node.next = Node(data) # 다음 노드를 생성

head = node1
for i in range(2,10):
    add(i)

node = head
while node.next:
    print(node.data)
    node = node.next
print(node.data)

node3 = Node(1.5)

node = head
search = True
while search:
    if node.data == 1:
        search = False
    else:
        node = node.next

node_next = node.next
node.next = node3
node3.next = node_next


node = head
while node.next:
    print(node.data)
    node = node.next
print(node.data)