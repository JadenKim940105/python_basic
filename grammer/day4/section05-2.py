# 파이썬 흐름제어 (반복문)

# for, while

v1 = 1
while v1 < 10:
    print(v1)
    v1 += 1

print('*' * 100)
v1 = 1
for i in range(1, 10):
    print("v1 is ", v1)
    v1 += 1

# 1 ~ 100 합

sum1 = 0
cnt = 1
while cnt <= 100:
    sum1 += cnt
    cnt += 1
print(sum1)

print(sum(range(1,101)))


# range, reversed, enumerate, filter, map, zip

names = ["kim", "park", "Cho", "Choi", "Yoo"]

for name in names:
    print(name)

word = "dreams"

for s in word:
    print(s)

my_info = {
    "name" : "kim",
    "age" : 33,
    "city" : "seoul"
}

# 기본값은 키가 출력됨
for key in my_info:
    print(key)

for value in my_info.values():
    print(value)

for item in my_info.items():
    print(item)


# KuuenESCbf : 소문자는 대문자로 대문자는 소문자로 출력하시오

str1 = "KuuenESCbf"

list1 = []

for s in str1:
    if s.isupper():
        list1.append(s.lower())
    else:
        list1.append(s.upper())

print("".join(list1))


# for - else
numbers = [1,2,3,4,11,34,234,34,23,6,567,23,88]

for num in numbers:
    if num == 99:
        print("99 Found")
        break
    else:
        print("99 not Fount")
else:
    print("no 99")



