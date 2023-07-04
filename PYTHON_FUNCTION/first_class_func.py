# def cat():
#     return "Meow"

# dog = cat #일급 함수
# print(dog())

# def app_op(func, a,b):
#     return func(a,b)

# def add(a,b):
#     return a+b

# def sub(a,b):
#     return a-b

# def multiply(a,b):
#     return a * b


# result = app_op(add,2,3)
# print(result)

# class User():
#     def __init__(self,id,name,pw,email,address) -> None:
#         self.id = id
#         self.name = name
#         self.pw = pw
#         self.email = email
#         self.address = address

#     def my_info(self):
#         print(self.id)
#         print(self.name)
#         print(self.pw)
#         print(self.email)
#         print(self.address)

# u_dict = {"id":"wqe123","pw":"123","email":"4_2@naver.com","name":"이준형","address":"대구"}
# player1 = User(**u_dict)
# player1.my_info()