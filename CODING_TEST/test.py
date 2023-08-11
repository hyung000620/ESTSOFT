# import sys
# from itertools import permutations

# n = int(input())
# guess_list = []
# for i in range(n):
#     guess_list.append(list(map(int, sys.stdin.readline().split())))

# items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# number_list = list(permutations(items, 3))

# success_number = []
# for i in guess_list:
#     number = i[0]
#     strike = i[1]
#     ball = i[2]
#     string_number = str(number)
#     first_number = string_number[0]
#     second_number = string_number[1]
#     third_number = string_number[2]
#     for idx, (j, k, l) in enumerate(number_list):
#         s = 0
#         b = 0
#         if j == int(first_number):
#             s += 1
#         else:
#             if str(j) in string_number:
#                 b += 1
#         if k == int(second_number):
#             s += 1
#         else:
#             if str(k) in string_number:
#                 b += 1
#         if l == int(third_number):
#             s += 1
#         else:
#             if str(l) in string_number:
#                 b += 1
        
#         if s== strike and b == ball:
#             pass
#         else:
#             number_list.remove(number_list[idx])


# print(len(number_list))

l = [1, 2, 3]
t = (4, 5, 6)

l[1]=10
l.append(7)
print(l)
t = t[:1]+(10,)+t[2:]
t += (7,)
print(t)