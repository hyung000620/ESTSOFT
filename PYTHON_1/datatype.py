'''
파이썬 가비지 컬렉터(Garbage Collector)는 파이썬 인터프리터가 자동으로 메모리 관리를 수행하는 기능입니다.
가비지 컬렉터는 동적으로 할당된 객체 중에서 더 이상 사용되지 않는 객체,
즉 가비지(garbage)라고 불리는 객체를 식별하고 회수하여 메모리를 해제합니다.
'''

# print(type())

# None
print(type(None))

#Bool
print(type(True))
print(type(False))

#숫자형
'''
제곱을 하면 음수가 되는 상상 또는 가상의 수인 허수(imaginary number)”를 고안하게 되었다.
i는 허수단위라 부르며, 수학에서는 영문자 허수의 i를 사용하지만 전기 분야에서는 전 류와 혼동되기 때문에 j로 사용한다

'''

print(type(5)) #정수 int
print(type(5.13)) #실수 float
print(type(2+3j)) #복소수 complex

#문자형
print(type("아무거나"))

#시퀀스
print(type((1,2,3)))
print(type([1,2,3]))

#dict
print(type({"A":10,"B":20}))

#set
print(type({"1","2","3"}))


print(type(b'abcd'))