'''
None
0 , 0.0
빈컨테이너
bool() -> False
'''

print(bool(0))
print(bool(1))
print(bool(0.0))
print(bool([]))
# 튜플 ()
print(bool(()))

number = 234234

if number:
    print("처리를 한다")
else:
    print("0이다")


number = 0
if number:
    pass
else:
    pass