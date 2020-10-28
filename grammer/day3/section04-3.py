#리스트와 튜플

#리스트 (순서ㅇ, 중복ㅇ, 수정ㅇ, 삭제ㅇ)
name1 = 'lee'
name2 = 'park'
names = ['lee', 'park']

a = []
print(type(a))
b = list()
print(type(b))
c = [1, 2, 3, 4]
d = ["hello", 1, 2, [1, 2, 3]]
print(c)
print(d)

# 인덱싱
print(d[0])
print(d[-1])
print(c[0] + c[1])

# 슬라이싱
print(d[0:3])
print(d[3][0:2])

# 연산
print(c + d)
print(c * 3)

c = [1, 2, 3, 4, 5]

c[1:2] = [100,1000]
print(c)
c[1] = [10,20]
print(c)

del c[1]
print(c)


print()
print('-' * 100)
print()


# 리스트 함수
y = [5, 2, 3, 1, 4]
print(y)
y.append(6)   # 끝에 추가
print(y)
y.sort()
print(y)
y.reverse()
print(y)
y.insert(2,7)   # 2번 index 에 7 추가
print(y)
y.remove(2)  # 해당 데이터 값을 지움 ( 2를 지움)
print(y)
print(y.pop())
print(y)    # 마지막 요소 제거

ex = [88,77]
y.extend(ex)
print(y)
y.append(ex)
print(y)

# 삭제 : del, remove, pop

# 튜플 (순서ㅇ , 중복ㅇ, 수정x, 삭제x)
a = ()
b = (1)
print(b)

c = (1,2,3,4)
d = (10, 100, ('a', 'b', 'c'))
print(d[2][0])

# 튜플 함수
z = (5,1,2,3,4,1)
print(z)
print(3 in z)
print(z.index(5))
print(z.count(1))
