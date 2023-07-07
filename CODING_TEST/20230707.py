# import sys
# n,m=map(int,sys.stdin.readline().split())
# cnt=[]
# for i in range(m):
#     a,b=map(int,sys.stdin.readline().split())
#     cnt.append(a)
#     cnt.append(b)
 
# for i in range(1,n+1):
#     print(cnt.count(i))

# while True:
#     s = input().replace(" ","")
#     if s == "#":break
    
#     cnt =0
#     s = set(s.lower())
#     for i in s:
#         if i.isalpha():
#             cnt+=1
            
#     print(cnt)

# n,m = map(int, input().split())

# arr=[]
# for i in range(n):
#     li=list(map(lambda x:x*2, input()))
#     arr.append("".join(li))

# for i in range(n):
#     if arr[i] != input():
#         print("Not Eyfa")
#         exit()

# print("Eyfa")

# def sol(album,s,e):
#     cnt = 0
#     answer=[]
#     for i in album:
#         if i[0]>=s and i[0]<=e:
#             cnt+=1
#             answer.append(i)
#         elif i[0]>e:
#             break
#     print(cnt)
#     for i in answer:
#         print(i[0],i[1])
# if __name__ == '__main__':
#     bowie = [[1967, 'DavidBowie'],
#              [1969, 'SpaceOddity'],
#              [1970, 'TheManWhoSoldTheWorld'],
#              [1971, 'HunkyDory'],
#              [1972, 'TheRiseAndFallOfZiggyStardustAndTheSpidersFromMars'],
#              [1973, 'AladdinSane'],
#              [1973, 'PinUps'],
#              [1974, 'DiamondDogs'],
#              [1975, 'YoungAmericans'],
#              [1976, 'StationToStation'],
#              [1977, 'Low'],
#              [1977, 'Heroes'],
#              [1979, 'Lodger'],
#              [1980, 'ScaryMonstersAndSuperCreeps'],
#              [1983, 'LetsDance'],
#              [1984, 'Tonight'],
#              [1987, 'NeverLetMeDown'],
#              [1993, 'BlackTieWhiteNoise'],
#              [1995, '1.Outside'],
#              [1997, 'Earthling'],
#              [1999, 'Hours'],
#              [2002, 'Heathen'],
#              [2003, 'Reality'],
#              [2013, 'TheNextDay'],
#              [2016, 'BlackStar']]
#     t= int(input())
#     for i in range(t):
#         s ,e =map(int,input().split())
#         sol(bowie,s,e)
    
# import sys
# from collections import deque

# n, k = map(int, input().split())

# deq = deque([i for i in range(1, n+1)])

# res = []
# while len(deq) != 0:
#     for _ in range(k-1):
#         deq.append(deq.popleft())
#     res.append(str(deq.popleft()))

# print('<'+', '.join(res)+'>')


# arr = [[0 for i in range(101)] for i in range(101)]

# for i in range(4):
#     x1,y1,x2,y2 = map(int, input().split())
#     for j in range(x1,x2):
#         for k in range(y1,y2):
#             arr[j][k]=1

# result = 0
# for i in arr:
#     result +=sum(i)
    
# print(result)

# n,m = map(int,input().split())
# a = [list(map(int,input().split()))for i in range(n)]

# m,k = map(int,input().split())
# b = [list(map(int, input().split())) for i in range(m)]

# for i in range(n):
#     result = []
#     for l in range(k):
#         tmp = 0
#         for j in range(m):
#             tmp += a[i][j] * b[j][l]
#         result.append(tmp)
#     print(*result)

# a,b = map(int, input().split())
# res = a*b

# while b:
#     a,b = b,a%b

# print(res//a)

# def gcd(x,y):
#     mod = x%y
#     while mod:
#         x= y
#         y= mod
#         mod = x%y
#     return y

# a,b = map(int, input().split())
# c,d = map(int, input().split())

# a = a*d+c*b
# b *=d

# n = gcd(a,b)
# print(a//n,b//n)

# import sys
# input = sys.stdin.readline

# n = int(input())

# stack=[]
# res = []
# for i in range(n):
#     li=input().split()
    
#     cmd = li[0]
#     if cmd =="push":
#         stack.append(li[1])
#     elif cmd == "top":
#         res.append(-1 if len(stack)==0 else stack[-1])
#     elif cmd == "size":
#         res.append(len(stack))
#     elif cmd == "pop":
#         res.append(-1 if len(stack)==0 else stack.pop())
#     elif cmd == "empty":
#         res.append(1 if len(stack)==0 else 0)

# print(*res, sep='\n')

# import sys
# from collections import deque

# input = sys.stdin.readline

# queue = deque()
# n = int(input())

# res = []
# for i in range(n):
#     li = input().split()

#     cmd = li[0]
#     if cmd == "push_back":
#         queue.append(li[1])
#     elif cmd == "push_front":
#         queue.appendleft(li[1])
#     elif cmd == "front":
#         res.append(queue[0] if len(queue) else -1)
#     elif cmd == "back":
#         res.append(queue[-1] if len(queue) else -1)
#     elif cmd == "size":
#         res.append(len(queue))
#     elif cmd == "empty":
#         res.append(0 if len(queue) else 1)
#     elif cmd == "pop_front":
#         res.append(queue.popleft() if len(queue) else -1)
#     elif cmd == "pop_back":
#         res.append(queue.pop() if len(queue) else -1)

# print(*res, sep='\n')

# def start_calculation(func):
#     def wrapper(*args, **kwargs):
#         print("아래 결과는?")
#         value = func(*args, **kwargs)
#         print("%0.2f" % value)
#     return wrapper

# @start_calculation
# def divide(a, b):
#        print(f"{a}를 {b}로 나누겠습니다.")
#        return  a / b

# divide(7, 3)