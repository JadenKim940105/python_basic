data_stack = list()

data_stack.append(1)
data_stack.append(2)

print(data_stack)

print(data_stack.pop())
print(data_stack.pop())


# 직접 push, pop 구현하기

stack = list()

def push(data):
    stack.append(data)

def pop():
    data = stack[-1]
    del stack[-1]
    return data

for i in range(10):
    push(i)

print(stack)

for i in range(len(stack)):
    print(pop())




