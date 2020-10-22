import datetime

# number = int(input())
#
# if number > 0:
#     print("{} 은 양수이다".format(number))
# elif number == 0:
#     print("{} 은 0이다".format(number))
# else:
#     print("{} 은 음수이다".format(number))

now = datetime.datetime.now()
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

# 오전 / 오후
if now.hour < 12:
    print('현재시간은 {}시 {}분으로 오전 입니다'.format(now.hour, now.minute))
else:
    print('현재시간은 {}시 {}분으로 오후 입니다'.format(now.hour, now.minute))

# in 을 사용한 홀수 / 짝수
number = input()

last_char = number[-1]

if last_char in ('13579'):
    print('홀수')
if last_char in ('02468'):
    print('짝수')
