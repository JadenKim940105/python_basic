import datetime
number = int(input("정수 입력 >> "))


# 조건 비교가 줄어들면 당연히 성능이 향상함, 따라서 else 를 쓸 수 있을 떈 사용하자.
if number % 2 == 0:
    print("짝수")
else:
    print("홀수")

# 파이썬에선 else if 대신 elif 사용
now = datetime.datetime.now()

if 3 <= now.month <=5:
    print("이번달은 {} 월로 봄입니다.".format(now.month))
elif 6<= now.month <= 8:
    print("이번달은 {} 월로 여름입니다.".format(now.month))
elif 8<= now.month <= 10:
    print("이번달은 {} 월로 가을입니다.".format(now.month))
else:
    print("이번달은 {} 월로 겨울입니다".format(now.month))
