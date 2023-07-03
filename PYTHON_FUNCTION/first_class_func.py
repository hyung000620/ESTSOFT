# def cat():
#     return "Meow"

# dog = cat #일급 함수
# print(dog())

def app_op(func, a,b):
    return func(a,b)

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multiply(a,b):
    return a * b


result = app_op(add,2,3)
print(result)
