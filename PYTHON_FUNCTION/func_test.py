# def greet(name):
#     print("반갑습니다 {} 여러분".format(name))
    
# greet("oreumi")

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multiply(a, b=2):
    return a*b

def sum(*args): # 가변인자
    total = 0
    for i in args:
        total +=i
    return total

def character_info(name, age):
    print("이름:",name)
    print("나이:",age)


result = add(1,3)
result = sub(3,2)
result = multiply(3)

result = sum(1,2,3,4,5,6)

character_info(age="ddd") #키워드 인자

print(result)