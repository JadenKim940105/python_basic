# 파이썬 클래스
# self, 클래스, 인스턴스 변수

# 선언
# class 클래스명:
#     함수
#     함수


class UserInfo:
    #속성, 메소드
    def __init__(self, name):
        self.name = name
    def user_info(self):
        print("Name: " + self.name)


user1 = UserInfo("kim")
user1.user_info()



# 클래스 변수, 인스턴스 변수

class WareHouse:
    stock_num = 0
    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1
    def __del__(self):
        WareHouse.stock_num -= 1


user1 = WareHouse("Kim")
user2 = WareHouse("Park")
user3 = WareHouse("Lee")

print(user1.name)
print(user1.stock_num)

del(user1)
print(user2.stock_num)



