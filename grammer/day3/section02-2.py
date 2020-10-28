# section02-2
# import this
import sys
# 파이썬 기본 인코딩 (입, 출력 기본값은 UTF-8)
print(sys.stdin.encoding)
print(sys.stdout.encoding)

# 출력
print("My name is Goodboy!")

# 변수 선언
myName = "goodBoy"
print(myName)

# 조건문
if myName == "goodBoy":
    print("okay")

# 함수
def func1():
    print("this is function")

func1()

# 클래스
class class1:
    pass

c1 = class1()

print(id(c1))