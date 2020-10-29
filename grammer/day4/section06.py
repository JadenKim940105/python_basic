# 파이썬 함수식 및 람다(lamda)

# 함수 정의 방법
# def 함수명(parameter):
# code

# 함수 호출
# 함수명(parameter)

def hello(param):
    print("hello,", param)


hello("python")


def helloReturn(param):
    val = "hello, " + str(param)
    return val


print(helloReturn("python!!"))


# 다중 리턴
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3


val1, val2, val3 = func_mul(100)
print(val1, val2, val3)


def func_mul2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]

l1 = func_mul2(100)
print(l1)


# 예제 4 *args, **kwargs

def args_func(*args):
    print(args)

args_func(1)
args_func(1,2)
args_func(1,2,1,'Park')

def args_func2(*args):
    for i, v in enumerate(args):
        print(i, v)

args_func2(1,2,3)

def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)

example_mul(1,2)
example_mul(1,2,1,2,3,4,4)
example_mul(1,2,12,1,key=1)


# 중첩함수

def nested_func(num):
    def func_in_func(num):
        print(num)
    print("in func")
    func_in_func(num + 1000)


nested_func(1000)


# 람다
# 람다식 : 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시실행(heap초기화)

# 일반함수
def mul_10(num):
    return 10 * int(num)

var_func = mul_10
print(type(var_func))
print(var_func(10))

# 람다식

lambda_mul_10 = lambda num: num * 10

print(lambda_mul_10(10))

def func_final(x, y, func):
    print(x * y * func(10))

func_final(10,10, lambda_mul_10)

print(func_final(10,10, lambda x : x * 1000))


add = lambda x,y : x + y
print(add(3,4))
print(add(4,5))

lamdas = [lambda x:x+10, lambda x:x+100]

print(lamdas[0](5), lamdas[1](5))

