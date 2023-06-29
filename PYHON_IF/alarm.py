# H, M =map(int, input().split())

# T = H*60+M-45

# if T<0: 
#     T+=24*60

# H,M=T//60,T%60

# print(H, M)

# h, m = map(int, input().split())
# t = int(input())

# f = (m+t)%60
# e = (h + (m+t)//60)%24
# print(e,f)

# A,B = map(int, input().split())
# C = int(input())

# total = A*60+B+C

# if total//60 > 23:
#     H=0
# else : 
#     H = total//60
# M = total%60

# print(H,M)

# H%24

# a,b,c=map(int,input().split())

# if (a==b and b==c) or (a==b or a==c):
#     print(10000+a*1000)
# elif b==c:
#     print(1000+b*100)
# else:
#     print(max(a,b,c)*100)
    
# 5번째 라인에 변수명이 H로 되어있습니다.
# HH, MM = map(int, input().split(" "))

# if MM < 45 :
#     if HH == 0:
#         HH = 23
#         MM += 15

#     else:
#         MM += 15
#         HH -= 1
# else:
#     MM -= 45

# print(HH, MM)

# n = int(input())
# print(((n-2)*(n-1)*(2*n-3)+3*(n-1)*(n-2))//12)
# print(3)

# a = [1,2,3,4,5]

# max_num = 0
# for i in a:
#     if max_num < i:
#         max_num = i
