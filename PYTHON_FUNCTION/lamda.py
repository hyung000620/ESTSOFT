# def add(a,b):
#     return a+b

# add = lambda a,b:a+b

# numbers = [1,2,3,4,5]
# squared = list(map(lambda x:x**2, numbers))

# print(squared)

student= [
    {"name":"이민영", "age":23},
    {"name":"양승조", "age":17},
    {"name":"문기원", "age":25},
]

student.sort(key=lambda x:x['age'])
print(student)