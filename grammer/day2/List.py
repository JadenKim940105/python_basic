# List - 순서가 있는 목록

# 파이썬에서는 하나의 리스트에 다양한 타입의 element 들이 들어갈 수 있다.
a = [1,2,'가','사과',True]
print(a[0])
print(a[-1])

# 이중 리스트
a = [[1,2,3],[4,5,6],[7,8,9]]
print(a[0])
print(a[0][1])

a = ["문자열"]
print(a[0][0])
print(a[0][1])
print(a[0][2])

# 리스트에 사용할 수 있는 연산자 : + , *
a = [1,2,3] + [4,5,6]
print(a)
a = [1,2,3] * 2
print(a)

# 리스트에 사용할 수 있는 연산자 : in, not in
a = [1,2,3,4]
print(3 not in a)
print(3 in a)


# 리스트의 함수 : append, insert, extend
a = [1, 2, 3]
a.append(4)
print(a)

a.insert(0,5)
print(a)

a.extend([5, 6, 7])
print(a)


# 비파과적 함수와 파괴적 함수

# 비파괴적 함수 ex) upper(), lower() (함수 실행 전과 실행 후 원본 값의 변경 없음)
a = 'hello'
a.upper()
print(a)
a = 'HELLO'
a.lower()
print(a)

# 파괴적 함수 ex) append(), insert(), extend() (함수 실행 전과 실행 후 원본 값의 변경 있음)
a = [1,2,3]
a.append(4)
print(a)


# 리스트 요소 제거 : 인덱스로 제거(del연산자, pop()), 값으로 제거(remove())
a = [1, 2, 3]
del a[1]
print(a)

a = [1, 2, 3, 4]
del a[0:3]
print(a)

a = [1, 2, 3, 4, 5, 6, 7]
a.pop(1)
print(a.pop()) # default pop(-1)
print(a)

a = [100, 200, 300, 400, 500]
a.remove(100)
print(a)

a = [1,1,1,1,1,1]
a.remove(1) # 동일 값이 여러개있을 경우 가장 좌측의 값 하나만 제거
print(a)
a.clear() # 전체 값 제거
print(a)




