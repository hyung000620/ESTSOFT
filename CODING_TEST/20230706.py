# k = int(input())

# for i in range(k):
#     n = int(input())
#     x = 2**n-1
#     print(x)


# def one_num(num):
#     if len(num)==1:
#         return num
#     else:
#         s = sum(list(map(int, num)))
#         return one_num(str(s))


# while True:
#     num = input()
#     if num == "0":break
    
#     print(one_num(num))
# import re

# text = "I love Programming. Today, I learn Crawling."

# pattern = r"\b\w+ing\b"
# result = re.findall(pattern, text)
# print(result)

# n = int(input())

# for i in range(n):
#     s = input().split()
#     s = s[2:]+s[:2]
#     print(*s,sep=' ')

# a,b = map(lambda x:x[::-1], input().split())

# n = abs(len(a)-len(b))

# if len(a)>len(b):
#     b += "0"*(len(a)-len(b))
# elif len(b)>len(a):
#     a += "0"*(len(b)-len(a))
    
# result = []
# for i in range(len(a)):
#     tmp = int(a[i])+int(b[i])
#     result.append(tmp)
    
# print(*result[::-1],sep='')



# while True:
#     bit = input()
#     if bit =="#":break
    
#     cnt = bit.count("1")
#     eo = bit[-1]
    
#     if cnt%2==0:
#         if eo =="e":
#             bit = bit.replace("e","0")
#         else:
#             bit = bit.replace("o","1")    
#     else:
#         if eo =="e":
#             bit = bit.replace("e","1")
#         else:
    #         bit = bit.replace("o","0")
    
    # print(bit)
# import sys
# input = sys.stdin.readline

# n = int(input())
# li = list(map(int,input().split()))

# arr = sorted(set(li))
# dic = {arr[i]: i for i in range(len(arr))}
# for i in li:
#     print(dic[i], end=' ')

# import sys

# N, M = map(int, sys.stdin.readline().strip().split())
# str = sys.stdin.read().split()
# S, command = set(str[:N]), str[N:]
# print(sum(1 for i in command if i in S))

# import sys

# input = sys.stdin.readline

# n,m = map(int, input().split())
# n_dic = {}
# for i in range(1,n+1):
#     p = input().strip()
#     n_dic[str(i)] = p
#     n_dic[p] = i

# li = []
# for i in range(m):
#     s = input().strip()
#     li.append(n_dic[s])
    

# print(*li,sep='\n')


# import sys

# input = sys.stdin.readline

# n,m = map(int, input().split())

# ns = set(input().strip() for i in range(n))
# ms = set(input().strip() for i in range(m))

# li = sorted(ns&ms)

# print(len(li))
# print(*li, sep='\n')


# s=input()
# n=len(s)
# se=set()
# for i in range(n):
#     for j in range(i,n):
#         se.add(s[i:j+1])

# print(len(se))

# while True:
#     li = input().split()
#     if li[0]=="0":break
#     arr=[]
#     arr.append(li[1])
#     for i in li[2:]:
#         if i != arr[-1]:
#             arr.append(i)
    
#     arr.append("$")
#     print(*arr, sep=' ')
    