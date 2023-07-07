def caculation(func):
    def wrapper(*args, **kwargs):
        print("데코레이터1 시작")
        func(*args, **kwargs)
        print("데코레이터1 종료")
    return wrapper

def caculation2(func):
    def wrapper(*args, **kwargs):
        print("데코레이터2 시작")
        func(*args, **kwargs)
        print("데코레이터2 종료")
    return wrapper

@caculation
@caculation2
def add(a,b):
    return a+b

@caculation
def minus(a,b):
    return a-b

@caculation
def muliply(a,b):
    return a*b

@caculation
def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "0으로 나눌 수 없습니다."


result = add(3,5)
print(result)

result = minus(3,5)
print(result)

result = muliply(3,5)
print(result)

result = divide(3,5)
print(result)