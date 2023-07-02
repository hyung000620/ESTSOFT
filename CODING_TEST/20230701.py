# import sys
# input = sys.stdin.readline

# arr = []
# while True:
#     x = float(input())
#     if x == -1.0:break
    
#     y = x/1000*167
#     arr.append(f"Objects weighing {x:0.2f} on Earth will weigh {y:0.2f} on the moon.")
    
# print(*arr, sep='\n')

# N = int(input())
# P = int(input())

# arr=[0]

# if N >=5: arr.append(500)
# if N>=10: arr.append(P//10)
# if N>=15: arr.append(2000)
# if N>=20: arr.append(P//4)

# result = P- max(arr)
# print(0 if result<0 else result)
'''
작은 두 변의 길이의 합이 제일 긴 변의 길이보다 커야 된다는 점을 사용하면 쉽게 풀 수 있다.
'''

# li = sorted(map(int, input().split()))
# res = li[0] + li[1] + min(li[2], li[0]+li[1]-1)
# print(res)

# fruits = ["용과", "포도", "석류"]
# people = ["은태", "남주", "미녀"]
# for idx, (fruit, person) in enumerate(zip(fruits, people)):
#      if idx == 1:
#           continue

# print(f"{person}는 {fruit}를 좋아해~")
    

# import sys
# input = sys.stdin.readline

# p,k=map(int, input().split())


# flag = True
# for i in range(2,k):
#     if p%i==0:
#         print(f"BAD {i}")
#         flag=False
#         break

# if flag:print("GOOD")

# n = int(input())

# for i in range(1,n+1):
#     st = input()
#     res = ""
#     for c in st:
#         val = ord(c)+1
#         if val > ord("Z"):val= ord("A")
#         res += chr(val)
#     print(f"String #{i}")
#     print(res)
#     print()

# for a in range(6,101):
#     for b in range(2,101):
#         for c in range(b+1,101):
#             for d in range(c+1,101):
#                 if a**3 == b**3 + c**3 + d**3:
#                     print(f"Cube = {a}, Triple = ({b},{c},{d})")
#                 if a**3 < b**3 + c**3 + d**3:
#                     break

# n = int(input())

# for i in range(1,n+1):
#     if 1+i+i**2==n:
#         print(i)
#         break

# import sys
# n=int(sys.stdin.readline())
# tmp=[]
# tmp.append(int(sys.stdin.readline()))
# for i in range(n):
#     a,b=map(int,sys.stdin.readline().split())
#     tmp.append( tmp[i]+a-b)
 
# for i in range(n+1):
#     if tmp[i]<0: print(0); exit()
# print(max(tmp))

# a,b,c,d=map(int, input().split())
# li = list(map(int, input().split()))

# for i in li:
#     cnt = 0
#     if 0<i%(a+b)<=a:cnt+=1
#     if 0<i%(c+d)<=c:cnt+=1
#     print(cnt)


# while 1:
#     try:
#         a,b,c = map(int, input().split())
#         num = max((b-a),(c-b))-1
#         print(num)
#     except:
#         break

# T = int(input())

# for i in range(T):
#     q = input()
#     n = int(input())
#     tmp = 0
#     for j in range(n):
#         tmp += int(input())
#     if tmp%n==0:print("YES")
#     else:print("NO")

# a_at,a_hp = map(int, input().split())
# b_at,b_hp = map(int, input().split())

# while a_hp>0 and b_hp>0:
#     a_hp-=b_at
#     b_hp-=a_at
    

# if a_hp>0:print("PLAYER A")
# elif b_hp>0:print("PLAYER B")
# else:print("DRAW")

# while 1:
#     li = list(map(int,input().split()))
#     if li[0] == 0:break
    
#     leaf=1
#     for i in range(1,len(li),2):
#         leaf = leaf * li[i] - li[i+1]
#     print(leaf)

# import sys
# input = sys.stdin.readline

# s1, s2 = map(int, input().split())
# li1 = [list(map(int, input().split())) for _ in range(s1)]
# li2 = [list(map(int, input().split())) for _ in range(s2)]
# for i in range(s1):
#     if li1[i][0] != li1[i][1]:
#         print("Wrong Answer")
#         exit()
# for i in range(s2):
#     if li2[i][0] != li2[i][1]:
#         print("Why Wrong!!!")
#         exit()
# print("Accepted")

# cnt = 1
# while 1:
#     a, b, c = map(int, input().split())
#     if a == b == c == 0:
#         break
#     if cnt > 1:
#         print()
#     print(f"Triangle #{cnt}")

#     if c == -1:
#         print("c = %.3f" % ((a**2+b**2)**0.5))
#     elif max(a, b) >= c:
#         print("Impossible.")
#     elif a == -1:
#         print("a = %.3f" % ((c**2-b**2)**0.5))
#     elif b == -1:
#         print("b = %.3f" % ((c**2-a**2)**0.5))    
#     cnt += 1
  

# H,W,N,M = map(int, input().split())

# garo = W//(M+1) if W%(M+1)==0 else W//(M+1)+1
# sero = H//(N+1) if H%(N+1)==0 else H//(N+1)+1

# print(garo *sero)

# N = int(input())

# s= 0
# for i in range(2,N-1,2):
#     s += (N-i-2)//2

# print(s)

# li = [1, 2, 3, 4]
# for c in input():
#     if c == 'A':
#         li[0], li[1] = li[1], li[0]
#     elif c == 'B':
#         li[0], li[2] = li[2], li[0]
#     elif c == 'C':
#             li[0], li[3] = li[3], li[0]
#     elif c == 'D':
#             li[1], li[2] = li[2], li[1]
#     elif c == 'E':
#             li[1], li[3] = li[3], li[1]
#     elif c == 'F':
#             li[2], li[3] = li[3], li[2]
# print(li.index(1)+1)
# print(li.index(4)+1)

# import sys
# input = sys.stdin.readline

# K,L = map(int, input().split())

# for i in range(2,L):
#     if K%i==0:
#         print(f"BAD {i}")
#         exit()

# print("GOOD")

# import sys
# input = sys.stdin.readline

# T = int(input())

# for i in range(1,T+1):
#     angle=""
#     li = sorted(map(int,input().split()))
    
    
#     if li[0]+li[1]<=li[2]:angle="invalid!"
#     elif li[0]==li[1]==li[2]: angle="equilateral"
#     elif li[0]==li[1] or li[1]==li[2]: angle="isosceles"
#     else: angle="scalene"
    
#     print(f"Case #{i}: {angle}")


# a,b,c,n = map(int, input().split())

# for i in range(n//a+1):
#     for j in range(n//b+1):
#         for k in range(n//c+1):
#             if a*i+b*j+c*k==n:
#                 print(1)
#                 exit()     
# print(0)

# t = int(input())

# for i in range(t):
#     x,y = input().split()

#     li=[]
#     for j in range(len(x)):
#         if ord(x[j])>ord(y[j]):
#             li.append(26-(ord(x[j])-ord(y[j])))
#         else:
#             li.append(ord(y[j])-ord(x[j]))
    
#     print("Distances:", *li)

# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# ac,bc = 0,0
# for i in range(len(a)):
#     if a[i]>b[i]:ac+=1
#     elif a[i]<b[i]:bc+=1

# if ac>bc:print("A")
# elif ac<bc:print("B")
# else: print("D")

# import sys
# input = sys.stdin.read

# s = input().replace("\n","").replace(" ","")
# c = [0] * 26
# for i in s:
#     c[ord(i)-97]+=1
    
# maxx = max(c)
# r = []
# for i in range(len(c)):
#     if c[i] == maxx:
#         r.append(chr(i+97))
        
# r.sort()
# print(*r,sep="")     

# t = int(input())

# for i in range(t):
#     li = sorted(map(int, input().split()))
       
#     if li[3]-li[1]>=4:print("KIN")
#     else:print(sum(li[1:4]))

# s = input()

# joi = 0
# ioi = 0
# for i in range(3,len(s)+1):
#     st = s[i-3:i]
#     if st == "JOI":joi+=1
#     elif st == "IOI":ioi+=1

# print(joi)
# print(ioi)

# for i in range(3):
#     li = str(input())
#     cnt = 1
#     max_num = 1
#     for i in range(7):  
#         if li[i]==li[i+1]:
#             cnt+=1
#         else:
#             max_num = max(max_num,cnt)
#             cnt=1
#     max_num = max(cnt, max_num)
#     print(max_num)

# p,s = input(),input()
# print(1 if s in p else 0)

# N, M, L = map(int, input().split()) # 5,3,2
# li = [0]*N
# cnt = i = 0
# while li[i] < M-1:
#     li[i] += 1
#     cnt += 1
#     print(*li, sep='')
   
#     i = (i+L)%N if li[i]%2 == 1 else (i-L)%N
# # print(cnt)

# N,M,L = map(int, input().split())

# li = [0]*N
# cnt = i = 0
# while li[i]<M-1:
#     li[i]+=1
#     cnt +=1
#     i = (i+L)%N if li[i]%2==1 else (i-L)%N
    
# print(cnt)

# n = int(input())

# for i in range(n):
#     s1,s2 = input().split()
#     s1,s2 = sorted(s1),sorted(s2)
    
#     print("Possible" if s1==s2 else "Impossible")

# print(bin(int(input()))[2:])

# e,f,c = map(int, input().split())

# tmp = (e+f)//c+ (e+f)%c
# cnt = (e+f)//c
# while tmp//c:
#     cnt += tmp//c
#     tmp = tmp//c+tmp%c
# print(cnt)

# n=int(input())
# r=0
# for i in range(1,n+1):
#     for j in range(i,n//i+1):         
#         r+=1
# print(r)

