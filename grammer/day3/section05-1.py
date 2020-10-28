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
