# Section 02-1
# 파이썬 기초
# Print 구문의 이해

# 기본출력
print('Hello Python!')
print("Hello Python!")
print("""Hello Python!""")
print('''Hello Pyhthon!''')
print()

# separator 옵션 사용
print('T', 'E', 'S', 'T', sep='')
print('2019', '02', '19', sep='-')
print('jaden', 'google.com', sep='@')

# end 옵션
print('Welcome To', end=' ')
print('the black parade', end='')

print()

# format 옵션 [], {}, ()
print('{} and {}'.format(10, '10'))
print("{0} and {1} and {0}".format('you', 'me'))
print("{a} and {b}".format(a='you', b='me'))

# %s: 문자 %d: 정수 %s: 실수
print("%s's favorite number is %d" %('jaden', 10))

print("Test1: %5d, price: %4.2f" % (776, 6534.123))
print("Test1: {0: 5d}, price: {1: 4.2f}".format(776, 6543.123))
print("Test1: {a: 5d}, price: {b: 4.2f}".format(a=776, b=6543.123))

"""
Escape 코드
\n : 개행
\t : tab 
"""
print("'you'")
print('\'you\'')

