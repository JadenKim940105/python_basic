# section04-2
# 문자열, 문자열 연산, 슬라이싱

str1 = "I am boy"
str2 = "niceMan"

print(len(str1), len(str2))

str3 = ""
print(len(str3))

str4 = str(123)
print(type(str4))

escape_str1 = "Do you have \"big collection\""
print(escape_str1)

# Raw String  -- escape 가 먹지 않는다.
raw_s1 = r'C:\programs\Test\Bin'
print(raw_s1)

raw_s2 = r"\\a\\b"
print(raw_s2)

# 멀티라인
multi = \
''' 
안녕
ㄴㄴㄴ
zz
'''
print(multi)


# 문자열 연산
str_o1 = "abc"
str_o2 = "def"
print(str_o1 + str_o2)
print(str_o1 * 10)

str_o4 = "hellojaden"
print('h' in str_o4)
print('a' not in str_o4)


# 문자열 함수

a = "NiceMan"
b = "orange"

print(a.islower())
print(b.endswith('e'))
print(a.capitalize())
print(a.replace('Nice', 'Good'))
print(list(reversed(b)))


print(a[0:3]) # 0,1,2 출력
print(a[0:4])
print(a[0:len(a)])
print(a[:4])
print(a[:])
print(b[0:4:2])
print(b[1:-2])
print(b[::-1])