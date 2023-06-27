# t = [list(map(int,input().split())) for _ in range(9)]

# max_num,max_row,max_col = 0,0,0

# for row in range(9):
#     for col in range(9):
#         if max_num <= t[row][col]:
#             max_num = t[row][col]
#             max_row = row+1
#             max_col = col+1

# print(max_num)
# print(max_row,max_col)

# N,M = map(int, input().split())
# boal = [0 for _ in range(N)]
# for b in range(M):
#     i,j,k = map(int, input().split())
#     for f in range(i,j+1):
#         boal[f-1] = k

# for i in range(N):
#     print(boal[i],end=' ')

# boal[2] = 3
# print(boal)

# N = int(input())
# for i in range(1,10):
#     print(f"{N} * {i} = {N*i}")

# V = int(input())
# s = input()
# A,B = 0,0
# for i in s:
#     if i == "A": A+=1
#     else: B+=1

# if A==B:print("Tie")
# elif A>B:print("A")
# else: print("B")

# N = int(input())

# for i in range(N):
#     k = int(input())
#     if k%2==0: print("even")
#     else : print("odd")
# from sys import stdin

# N = int(stdin.readline())
# print(N*N)
# print(2)

# from sys import stdin

# alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# arr = list(alphabet)
# ask = [i for i in range(65,91)]

# T = int(stdin.readline())

# for i in range(T):
#     sum = 0
#     stdin.readLine()

# from sys import stdin

# N = stdin.readline()

# N = int(input())
# for i in range(N):
#     s = input()
#     l = len(s)//2
#     if s[l] == s[l-1]: print("Do-it")
#     else: print("Do-it-Not")

# n = int(input())
# for i in range(n):
#     x,y = map(int,input().split())
#     if x>=y:print("MMM BRAINS")
#     else: print("NO BRAINS")

# N = int(input())
# arr = list(map(int, input().split()))
# arr.sort()
# print(arr[-1])

# while True:
#     N = int(input())
#     tmp = 0
#     if N == 0: break
#     else:
#         for i in range(N+1):
#            tmp += i*i
#         print(tmp)

# d2 = input().upper()

# if 'D2' in d2 :print("D2")
# else:print("unrated")

# N = int(input())
# s="뭐야?"
# for i in range(N):
#     if input() == "anj":s="뭐야;"

# print(s)

# num = input()
# level = 0
# while True:
#     if len(num) == 1:break
#     tmp = 1
#     for t in num:
#         tmp *= int(t)
#     level +=1
#     num = str(tmp)
# print(level)

# N = int(input())
# S = input()
# print(S[-5:])

# l = int(input())
# s = input().count("2")
# t = l-s

# if s==t:print("yee")
# elif s>t:print(2)
# else:print("e")

# while 1:
#     A,B = map(int, input().split())
#     if A==0 & B==0:break
    
#     print(A-(B-A))

# T = int(input())

# for i in range(T):
#     n, m = input().split()
#     n = float(n)
#     if m == "kg":print(f"{n*2.2046:0.4f} lb")
#     elif m == "lb":print(f"{n*0.4536:0.4f} kg")
#     elif m == "l":print(f"{n*0.2642:0.4f} g")
#     else:print(f"{n*3.7854:0.4f} l")
import sys

N,X,K = map(int, sys.stdin.readline().split())
cup = [0]*(N+1)
cup[X] = 1
for i in range(K):
    A,B= map(int, sys.stdin.readline().split())
    cup[A],cup[B]=cup[B],cup[A]

print(cup.index(1))