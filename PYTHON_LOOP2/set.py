numbers = [1, 2, 2, 3, 3, 5]
set_numbers = set(numbers)

# print(len(set_numbers))

a = {1,2,3,5}
b = {3,5,6,7}

# print(a.intersection(b)) #교집합

# print(a.union(b)) #합집합

# print(a.difference(b)) #차집합

# a.add(4)
# a.remove(3)
# a.discard(5)

# is_sub = a.issubset(b) #부분집합
# print(a)

a = [1,2,3]
print(*a, sep='\n')