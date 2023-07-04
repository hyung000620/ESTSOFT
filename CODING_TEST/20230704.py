# k = int(input())

# for i in range(k):
#     p,m = map(int, input().split())
#     li = [0]*(m+1)
    
#     cnt =0
#     for j in range(p):
#         t = int(input())
#         if li[t]==0:
#             li[t]+=1
#         else:
#             cnt+=1
#     print(cnt)

# t = int(input())

# for i in range(t):
#     a,b = input(),input()
    
#     cnt = 0
#     for i in range(len(a)):
#         if a[i]!=b[i]:cnt+=1
#     print(f"Hamming distance is {cnt}.")

# n = int(input())
# s = input()
# score = cnt = 0
# for i in range(1,n+1):
    
#     if s[i-1]=='O':
#         score += i+cnt
#         cnt+=1
#     else:
#         cnt =0
# print(score)


# st = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# n,b = map(int,input().split())

# result =""
# while n>0:
#     tmp = n%b
#     n//=b
#     result+=st[tmp]
    
# print(result[::-1])

# a,b=map(int,input().split())
# c=int(input())
# n=int(input())
# r=1 if a*n+b<=c*n and c>=a else 0
# print(r)




n = int(input())
print(2**n -1)
def hanoi(n,시작,보조,목표):
    if n==1:
        print(시작, 목표)
        return
    else:
        hanoi(n-1,시작,목표,보조)
        print(시작,목표)
        hanoi(n-1,보조,시작,목표)

hanoi(n,1,2,3)