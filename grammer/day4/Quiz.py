# 1. 아래 문자열의 길이를 구해보세요
q1 = "3dnfadsjkgbjbjhas24hjbdng2413sdva"
print(len(q1))

# 2. print 함수를 사용해서 아래와 같이 출력해보세요
print('{};{};{};{}'.format('apple', 'orange', 'banana', 'lemon'))
# print("""apple;orange;banana;lemon""")

# 3. 화면에 * 기호를 100개 표시하세요
print('*' * 100)

# 4. 문자열 "30" 을 각각 정수형, 실수형, 복소수형, 문자형으로 변환해보세요
str1 = "30"
int1 = int(str1)
print(int1)
print(type(int1))

float1 = float(str1)
print(float1)
print(type(float1))

complex1 = complex(str1)
print(complex1)
print(type(complex1))

print(str1)
print(type(str1))

# 5. 다음 문자열 "Niceman" 에서 "man" 문자열만 추출해보세요
str1 = "Niceman"
print(str1[str1.index("man"):])
print(str1[4:])


# 6. 다음 문자열을 거꾸로 출력해보세요 : "Strawberry"
str1 = "Strawberry"
list1 = list(str1)
list1.reverse()
print("".join(list1))
print(str1[::-1])

# 7. 다음 문자열에서 '-' 를 제거 후 출력하세요 : "010-7777-9999"
str1 = "010-7777-9999"
print(str1[0:3] + str1[4:8] + str1[-4:])

# 정규표현식

import re
print(re.sub('[^0-9]','',str1))

# 8. 다음 문자열(URL)에서 "http://" 부분을 제거 후 출력하세요: : "http://daum.net"

str1 = "http://daum.net"
print(str1[7:])


# 9. 다음 문자열을 모두 대문자, 소문자로 표시해보세요 : "NiceMan"
str1 = "NiceMan"
print(str1.upper())
print(str1.lower())

# 10. 다음 문자열 슬라이싱을 이용해서 "cde"만 출력하세요 : "abcdefghijklmn"
str1 = "abcdefghijklmn"
print(str1[str1.index("cde"):str1.index("cde")+3])

# 11. 다음 리스트에서 "Apple" 항목만 삭제하세요 : ["Banana", "Apple", "Orange"]
list1 = ["Banana", "Apple", "Orange"]
list1.remove("Apple")
print(list1)


# 12. 다음 튜플을 리스트로 변혼하세요 : (1, 2, 3, 4)
tuple1 = (1, 2, 3, 4)
list1 = list(tuple1)
print(list1)

# 13. 다음 항목을 딕셔너리로 선언해보세요 : <성인 - 10000, 청소년 - 7000, 아동 - 3000>
dict1 = {
    "성인":10000,
    "청소년":7000,
    "아동":3000
}
print(dict1)

# 14. 13번 에서 선언한 dict 항목에 <소아 - 0 > 항목을 추가해보세요
dict1['소아'] = 0
print(dict1)

# 15. 13번 에서 선언한 dict 항목에 key 항목만 출력해보세요
print(dict1.keys())

# 16. 13번 에서 선언한 dict 항목에 value 항목만 출력해보세요
print(dict1.values())