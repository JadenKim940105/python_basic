# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 = fruit = {"봄": "딸기", "여름": "토마토", "가을": "사과"}

print(fruit.get("가을"))



# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 = fruit = {"봄": "딸기", "여름": "토마토", "가을": "사과"}

for item in fruit.items():
    if item.__contains__("사과"):
        print("포함됨")


# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점
score = 40

if score > 80:
    print("A학점")
elif score > 60:
    print("B학점")
elif score > 40:
    print("C학점")
elif score > 20:
    print("D학점")
else:
    print("E학점")

# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18
a, b, c = 12, 6, 18

if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else: # b > a
    if b > c:
        print(b)
    else:
        print(c)
print(max(a, b, c))

# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)

jumin = 9401051201010

str1 = str(jumin)
if str1[6:7] == "1" or str1[6:7] == "3":
    print("남자")
else:
    print("여자")

print(str1[6])
if int(str1[6]) % 2 == 0:
    print("여자")
else:
    print("남자")




# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]

for i in q3:
    if i == "정":
        continue
    else:
        print(i)

# '정' 을 제외하고 리스트로 만들어라

list3 = [x for x in q3 if x != '정']
print(list3)



# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
for i in range(1, 101):
    if i % 2 == 1:
        print(i, end=' ')
print()

# 1~100 사이의 수  홀수만 리스트로 만들어라 중 (리스트컴프리핸션 사용)

list7 = [x for x in range(1, 101) if x % 2 == 1]
print(list7)



# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]

for i in q4:
    if len(i) >= 5:
        print(i, end=' ')



print()

# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for i in q5:
    if i.islower():
        print(i, end=' ')

print()


# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for i in q6:
    if i.islower():
        print(i.upper(), end=' ')
    else:
        print(i.lower(), end=' ')


print()
print()
print()
print()

# 리스트 컴프리핸션

numbers = []
for n in range(1, 11):
    numbers.append(n)
print(numbers)

numbers2 = [x for x in range(1, 11)]
print(numbers2)
