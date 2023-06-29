# with open("test.txt","r") as f:
    
#     arr = []
#     for line in f:
#         l = line.replace('\n',"")
#         arr.append(l)
#     arr.sort()
    
#     print(f"전체 개수: {len(arr)}")
#     arr = set(arr)
#     print(f"중복을 제가하고 남은 개수: {len(arr)}")
'''
연립방정식

Ax +By = C  
Dx +Ey = F

x = (C * E - B * F) // (A * E - B * D)
y = (A * F - C * D) // (A * E - B * D)
'''

# a,b,c,d,e,f=map(int, input().split())

# for x in range(-999,1000):
#     for y in range(-999,1000):
#         if a*x+b*y==c and d*x+e*y==f:
#             print(x,y)

# a = 1
# b = 1
# c = 1

# if a is c: print("True")

# if a is None:
#     print("True")
# if type(a) == "<class 'NoneType'>":
#     print("True")
# if type(a) == None:
#     print("True")

# print(type(a))
# print(type(str))
# print(type(a))
 
 
# a = [1,2,3]
# b = a
# c = [1,2,3]
# n = int(input())
# match n:
#     case 1: print("1111")
#     case 2: print("2222")
#     case 3: print("3333")
#     case 4: print("4444")
#     case 5: print("5555")
#     case 6: print("6666")
        
# print(a==b) # 값이 같으므로 True
# print(a==c) # 값이 같으므로 True
# print(a is b) # 같은 객체를 가리키기 때문에 True
# print(a is c) # 다른 객체를 가리키기 때문에 False
# score = 22
# if score in range(20,30):print("d")


# x = int(input())
# y = int(input())
# if x>0:
#     if y>0: print(1)
#     else: print(4)
# else:
#     if y>0: print(2)
#     else: print(3)

# N = int(input())

# import sys
# input = sys.stdin.readline

# res=[]
# for _ in range(int(input())):
#     li = list(map(int,input().split()))

#     st = len(set(li))
#     if st == 1:
#         res.append(50000+li[0]*5000)
    
#     elif st == 2:
#         count = li.count(max(li))
#         if count ==1:
#             res.append(min(li)*1000 + 10000)
#         elif count ==3:
#             res.append(max(li)*1000 + 10000)
        
#         elif count ==2:
#             res.append(max(li)*500+ min(li)*500 + 2000)
#     elif st == 3:
#         for p in li:
#             if li.count(p) == 2:
#                 res.append(p*100+1000)
#                 break
#     else:
#         res.append(max(li)*100)
        
# print(max(res))

# N, M = map(int, input().split())
# arr = [0 for i in range(N+1)]
# for _ in range(M):
#     i,j,k = map(int, input().split())
#     for x in range(i,j+1):
#         arr[x] = k
        
# for i in arr[1:]:
#     print(i, end=' ')

# N, M = map(int, input().split())
# arr = [i for i in range(1,N+1)]

# for i in range(M):
#     i,j = map(int, input().split())
#     arr[i-1],arr[j-1]=arr[j-1],arr[i-1]

# print(*arr)

#7
# T = int(input())
# for i in range(T):
#     R,S = input().split()
#     for c in S:
#         print(c*int(R),end='')
#     print()

#8
# st = list(map(str,input().split()))
# print(len(st))

#9
# A,B = input().split()
# ra,rb = int(A[::-1]),int(B[::-1])
# print(ra if ra>rb else rb)

#10
# a=input()
# b=['ABC','DEF','GHI','JKL','MNO', 'PQRS','TUV','WXYZ']
# c=0
# for i in range(len(a)):
#   for j in range(8):
#     if a[i] in b[j]:
#       c+=j+3
#       continue
# print(c)

#11
import sys
for line in sys.stdin:
    sys.stdout.write(line)