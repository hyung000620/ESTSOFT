# N = int(input())

# #for문 활용
# sum = 0
# for i in range(1,N+1):
#     sum +=i
# print(sum)

# #수학공식 활용
# print(N*(N+1)//2)

# #5
# for i in range(int(input())//4):
#     print("long", end=" ")
    
# print("int")
# #6
# import sys

# t = int(sys.stdin.readline())

# for i in range(t):
#     a,b = map(int, sys.stdin.readline().split())
#     print(a+b)
# #7
# import sys

# N = int(sys.stdin.readline())

# for i in range(N):
#     A,B = map(int, sys.stdin.readline().split())
#     print(f"Case #{i+1}: {A+B}")
    
# #8
# import sys

# N = int(sys.stdin.readline())

# for i in range(N):
#     A,B = map(int, sys.stdin.readline().split())
#     print(f"Case #{i+1}: {A} + {B} = {A+B}")

#문자열3
# T = int(input())
# for i in range(T):
#     s = input()
#     print(f"{s[0]}{s[-1]}")
#문자열4
# print(ord(input()))
#문자열5
# N = int(input())
# S = input()
# result = 0
# for i in S:
#     result += int(i)
# print(result)

N = int(input())

sum = N*(N+1)//2
print(sum/N)