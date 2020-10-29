# 파이썬 자료구조 (리스트, 튜플, 딕셔너리, 집합)

# 딕셔너리(Dictionary) : 순서x, 중복x, 수정ㅇ, 삭제ㅇ

# 선언
a = {'name':'kim', 'phone':'010-1111-2222', 'birth':940105}
b = {0: 'Python', 1: "Java"}
c = {'arr': [0, 1, 2, 3]}
print(a)
print(b)
print(c)


# key 로 찾는다
print(a['name'])
print(a.get('name'))
print(a.get('name1'))

print(c.get('arr')[0:2])

#딕셔너리 추가
a['address'] = 'seoul'
print(a)
a['rank'] = [1,2,3]
a['rank2'] = (1,2,3)
print(a)

print(a.keys())
print(type(a.keys()))
temp = (list(a.keys()))
print(temp[1:3])


# 집합 (순서x, 중복x)
a = set()
b = set([1,2,3,4])
c = set([1,4,5,6,6])
print(type(b))
print(c)

t = tuple(b)
print(t)
l = list(b)
print(l)

print()
print()

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print(s1.intersection(s2)) # 교집합
print(s1 & s2) # 교집합

print(s1 | s2)  # 합집합
print(s1.union(s2)) # 합집합

print(s1 - s2) # 차집합
print(s1.difference(s2)) # 차집합

s3 = set([7,8,10,15])
s3.add(18)
print(s3)
s3.add(6)
print(s3)
s3.remove(10)
print(s3)


l2 = list(s3)
print(l2)
print(l2[0:3])