# '문자열{}'.format()
print("{}년{}월{}일{}요일".format(2020,10,23,'금'))
# {} 이 매개변수보다 많으면 out of index

# 대소문자 바꾸기 upper(), lower()
str1 = 'hello this is jaden'
print(str1.upper())
str2 = 'HELLO THIS IS JADEN'
print(str2.lower())

# strip() = trim()  양쪽 공백 제거
print("    hello world     ".strip())
# lstrip() / rstrip() 왼쪽 / 오른쪽 공백만 제거

# find() 문자열 중 몇번째 index 에 해당 원소가 있는가 없을시 -1
print('가나다라마바사가나다라마바'.find('다'))

# rfind() 오른쪽부터 찾아서 몇번재 index 에 해당 원소가 있는지 반환
print('가나다라마바사가나다라마바'.rfind('다'))

# in() 타겟 문자열이  대상 문자열안에 있나?
print('가' in '가나다라')
print('가나' in '가나다라')

# split('') ''안으로 잘라서 리스트형태로
str = '10,20,30,40'
print(str.split(','))


# a = int(input("> 1번째 숫자 : "))
# b = int(input("> 2번째 숫자 : "))
# print('{} + {} = {}'.format(a, b, a+b))

print('----')

string = 'hello'
string.upper()
print(string)
print(string.upper())

