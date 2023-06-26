'''
변수를 다시 선언하면
메모리를 재할당하게 된다.
'''

str1 = "hello"
str2 = " world!"

# print(id(str1))
# print(str1 + str2)

str1 = "출석체크 입니다.\n" *10

# print(id(str1))
# print(str1)

str1 = "여기서 a는 몇번째 일까요?"
print(str1[4])

str1 = "여기서 apple은 어디서부터 어디까지 일까요?"
print(str1[4:8])
print(str1[9:])
print(str1[:4])

print(len(str1))

