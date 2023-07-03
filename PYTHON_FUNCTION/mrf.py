from functools import reduce
# map(func, list or tupple)

# reduce
# numbers = [1,2,3,4,5]
# sum = reduce(lambda x,y:x+y, numbers)
# print(sum)

# filter

# numbers =[1,2,3,4,5]
# numbers = filter(lambda x:x%2, numbers)
# print(*numbers)

numbers = ["letter","bigger"]

numbers = list(map(lambda x:x.upper(),numbers))
print(numbers)