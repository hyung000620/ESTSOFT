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




# n = int(input())
# print(2**n -1)

# def hanoi(n,start,end):
#     middle = 6-start-end
#     if n==1:
#         print(start, end)
#         return
#     else:
#         hanoi(n-1,start,middle) #1번->2번
#         print(start,end) #1번->3번
#         hanoi(n-1,middle,end) #2번->3번

# hanoi(n,1,3)


# s = input()
# print("true" if s==s[::-1] else "false")

# s = input()
# print(s[:s.index("(")].count("@"), s[s.index(")"):].count("@"))



# n =int(input())

# for i in range(n):
#     s = input()
#     if s =="P=NP":print("skipped")
#     else: print(sum(list(map(int,s.split("+")))))


# n = int(input())

# cnt = 1
# for i in range(n):
#     li = list(map(int,input().split()))
#     sum = 0
#     for j in range(1,len(li)+1):
#         if ((j-1)%5)+1 == li[j-1]:
#             sum+=1

#     if sum == len(li):
#         print(cnt)
    
#     cnt+=1
# n,k= map(int, input().split())

# li = list(map(lambda x:int(str(x)[::-1]), range(n,n*k+1,n)))

# print(max(li))

# n = int(input(),2)
# print(oct(n)[2:])

# n = int(input())

# for i in range(n):
#     l,d = input().split("-")
#     l = list(map(lambda x: ord(x)-65, l))
#     sum = l[0]*676+l[1]*26+l[2]-int(d)
#     print("nice" if abs(sum)<=100 else "not nice")

# n = int(input())
# for i in range(n):
#     li = ["god"]
#     li += input().split()[1:]
#     print(*li,sep='')

# n = int(input())
# li = [int(input()) for i in range(n)]

# if li[1]-li[0]==li[2]-li[1]:
#     tmp = li[1]-li[0]
#     print(li[-1]+tmp)
# else:
#     tmp = li[1]//li[0]
#     print(li[-1]*tmp)

# while 1:
#     s = input()


# while True:
#     st = set(input().replace(" ",""))
#     if "*" in st:break
#     print("Y" if len(st)==26 else "N")

# n=int(input())%2
# s1,s2=input(),input()

# T,F ="Deletion succeeded","Deletion failed"

# if n:
#     s1.replace("0","2").replace("1","0").replace("2","1")
#     print(T if s1==s2 else F)
# else:
#     print(T if s1==s2 else F)


# n = int(input())
# li = [[0 for i in range(n)] for i in range(n)]

# fnd = int(input())

def hanoi(s,m,e,n):
    if n == 1:
        print(s,e)
    else:
        hanoi(s,e,m,n-1)
        print(s,e)
        hanoi(m,s,e,n-1)
