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
# import sys

# N,X,K = map(int, sys.stdin.readline().split())
# cup = [0]*(N+1)
# cup[X] = 1
# for i in range(K):
#     A,B= map(int, sys.stdin.readline().split())
#     cup[A],cup[B]=cup[B],cup[A]

# print(cup.index(1))


# import sys
# input = sys.stdin.readline

# t = int(input())

# for _ in range(t):
#   alphabet = [0] * 27
#   value = input().rstrip()
#   for i in range(len(value)):
#     alphabet[int(ord(value[i])) - 65] += 1

#   result = 0
#   for i in range(26) :
#     if alphabet[i] == 0 :
#       result += i + 65

#   print(result)



# N,M = map(int, sys.stdin.readline().split())
# arr=[0]*(N+1)
# for i in range(M):
#     A,B = map(int, sys.stdin.readline().split())
#     arr[A]+=1
#     arr[B]+=1

# for i in range(1,N+1):
#     print(arr[i])


# N = int(input())
# text=[]

# text.append("int a;")
# text.append("int *ptr = &a;")
# if N>1:
#     for i in range(2,N+1):
#        star = "*"*i
#        p=i-1
#        if p==1:p=""
#        text.append(f"int {star}ptr{i} = &ptr{p};") 

# for i in range(len(text)):
#     print(text[i])

# score = list(map(int, input().split()))

# max_score = [100,100,200,200,300,300,400,400,500]
# h = False
# for i in range(9):
#     if score[i] > max_score[i]:
#         h = True
#         break
# if h : print("hacker")
# elif sum(score) <100:print("none")
# else : print("draw")

# n = int(input())
# arr = []
# for i in range(n):
#     name,score=input().split()
#     score= int(score)
#     if score >96: arr.append(f"{name} A+")
#     elif score >89: arr.append(f"{name} A")
#     elif score >86: arr.append(f"{name} B+")
#     elif score >79: arr.append(f"{name} B")
#     elif score >76: arr.append(f"{name} C+")
#     elif score >69: arr.append(f"{name} C")
#     elif score >66: arr.append(f"{name} D+")
#     elif score >59: arr.append(f"{name} D")
#     else: arr.append(f"{name} F")

# print(*arr,sep='\n')

# import sys
# input = sys.stdin.readline

# T = int(input())
# for i in range(T):
#     sum = 0
#     for day in range(int(input())):
#         tmp = list(map(int, input().split()))
#         if max(tmp)>0:sum+=max(tmp)
#     print(sum)

# s=0
# while True:    
#     try:       
#         _ = input()        
#         s+=1    
#     except EOFError:        
#         break
# print(s)

# import sys
# input = sys.stdin.readline

# N = int(input())
# mirror = [input().strip() for _ in range(N)]
# K= int(input())

# if K==1:print(*mirror,sep='\n')
# elif K==2:print(*[i[::-1] for i in mirror],sep='\n')
# else: print(*mirror[::-1],sep='\n')

# import sys
# input = sys.stdin.readline

# T = int(input())
# result = []
# for i in range(1,T+1):
#     good = list(map(int,input().split()))
#     evil = list(map(int,input().split()))
#     good_score = good[0] + good[1]*2 + good[2]*3 + good[3]*3 + good[4]*4 + good[5]*10
#     evil_score = evil[0] + evil[1]*2 + evil[2]*2 + evil[3]*2 + evil[4]*3 + evil[5]*5 + evil[6]*10
    
#     if good_score<evil_score: result.append(f"Battle {i}: Evil eradicates all trace of Good")
#     elif good_score>evil_score:result.append(f"Battle {i}: Good triumphs over Evil")
#     else: result.append(f"Battle {i}: No victor on this battle field")

# print(*result,sep='\n')

import sys
input = sys.stdin.readline

def factorial(n):
    sum = 1
    for i in range(1,n+1):sum*=i
    return sum

result = []
while 1:
    a = input().strip()
    if int(a) == 0: break
    
    tmp = 0
    r_a = a[::-1]
    for idx, i in enumerate(r_a,start=1):
        tmp += factorial(idx)*int(i)
    result.append(tmp)

print(*result,sep='\n')