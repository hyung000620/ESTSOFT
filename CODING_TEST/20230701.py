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


