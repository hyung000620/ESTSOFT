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
# import sys
# for line in sys.stdin:
#     sys.stdout.write(line)
    
# [], 1, "False", {}, None, not True, [None]

# N = int(input())
# A = list(map(int, input().split()))
# B,C = map(int, input().split())

# num=N
# for i in A:
#     i-=B
#     if i>0:
#         if i%C: num+=(i//C)+1
#         else: num +=(i//C)

# print(num)

# t = int(input())  # 테스트 케이스의 개수

# for _ in range(t):
#     n, k, x = map(int, input().split())  # n, k, x 입력받기

#     if (k-1) * (k-2) // 2 >= n-1:  # 가능한 경우인지 확인
#         print("NO")
#     else:
#         print("YES")
#         taken = []
#         for i in range(1, k+1):
#             if i != x:
#                 taken.append(i)
#                 n -= i
#                 if n == 0:
#                     break
#         print(len(taken))
#         print(" ".join(map(str, taken)))

# S = input()

# result=""
# for c in S:
#     tmp = c
#     if ord("A")<=ord(c)<=ord("Z"):
#         tmp = ord(c)+13
#         if ord("Z")<tmp: tmp=ord("A")+(tmp-ord("Z")-1)
#         tmp = chr(tmp)
#     elif ord("a")<=ord(c)<=ord("z"):
#         tmp = ord(c)+13
#         if ord("z")<tmp: tmp=ord("a")+(tmp-ord("z")-1)
#         tmp = chr(tmp)
        
#     result+=tmp
        
# print(result)

# result=[]
# while True:
#     n = int(input())
#     if n == -1: break
#     li = []
#     li.append(1)
#     for i in range(2,n//2):
#         if n%i==0:
#             li.append(i)
#             li.append(n//i)
#     li = list(set(li))
#     li.sort()
#     if n == sum(li):
#         st = " + ".join(map(str, li))
#         result.append(f"{n} = {st}")
#     else:
#         result.append(f"{n} is NOT perfect.")

# print(*result,sep='\n')

# n = input()

# # 2진수 -> 10진수 변환 
# d = int(n,2)

# # 10진수 -> 8진수 변환 
# print(oct(d)[2:])

# num = list(map(int, input().split()))

# while True:
#     if num == [1,2,3,4,5]:break
#     for i in range(len(num)-1):
#         if num[i]>num[i+1]:
#             num[i],num[i+1]=num[i+1],num[i]
#             print(*num,sep=' ')

# def Rev(x):
#     return int(x[::-1])
# X,Y = input().split()
# result = Rev(X)+Rev(Y)
# result = Rev(str(result))
# print(result)

# N = int(input())
# for i in range(1,N+1):
#     arr = list(map(str, input().split()))
#     arr = arr[::-1]
#     st = " ".join(arr)
#     print(f"Case #{i}: {st}")

# s = input()
# sad = s.count(":-(")
# happy = s.count(":-)")

# if sad == 0 and happy == 0:print('none')
# elif sad > happy:print("sad")
# elif sad < happy:print("happy")
# elif sad == happy: print("unsure")


# s1, s2 = map(str, input().split())

# for i in range(len(s1)):
#     if s1[i] in s2:
#         col = i
#         row = s2.index(s1[i])
#         break
    
# for i in range(len(s2)):
#     if i == row:
#         print(s1)
#     else:
#         print('.'*col + s2[i] + '.'*(len(s1)-col-1))
# s = ''
# while 1:
#     try:
#         s += input()
#     except:
#         break
# print(sum(map(int, s.split(','))))

# H1,M1,S1=map(int, input().split(":")) #현재 시간
# H2,M2,S2=map(int, input().split(":")) #임무를 시작한 시간

# rh,rm,rs=0,0,0
# S2-S1

#3
'''
```py
def MenOfPassion(A,n):
    sum = 0
    for i in range(n):
        for j in range(n):
            sum += A[i]*A[j]
    return sum
```
'''
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = arr[:mid]
#     right = arr[mid:]
#     left = merge_sort(left)
#     right = merge_sort(right)
#     return merge(left, right)

# def merge(left, right):
#     result = []
#     i = j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     print(result)
#     return result


# arr=[1,4,6,2,3,5,6,8]
# arr = merge_sort(arr)
# print(arr)


# def MenOfPassion(A,n):
#     cnt = 0
#     for i in range(n-1):
#         for j in range(i+1,n):
#             cnt +=1
#     return cnt

# A=[1,2,3,4,5,6]
# n = len(A)
# print(MenOfPassion(A,n))

'''
n: 2, 1번수행
n: 3, 3번수행
n :4, 6번수행
n :5, 10번 수행
n :6, 15번수행
'''
# n = int(input())

# print(int((n-1)*n-(n-1)*n/2))
# print(2)
# #5
# def MenOfPassion(A, n):
#     sum = 0
#     for i in range(n):
#         for j in range(n):
#             for k in range(n):
#                 sum += A[i] * A[j] * A[k]
#     return sum
# #6
# def MenOfPassion(A, n):
#     sum = 0
#     for i in range(n-2):
#         for j in range(i+1, n-1):
#             for k in range(j+1, n):
#                 sum += A[i] * A[j] * A[k]
#                 print(A[i],A[j],A[k])
#     return sum

# A=[1,2,3,4,5]
# n = len(A)
# MenOfPassion(A,n)
'''
n: 2, 0번수행
n: 3, 1번수행
n :4, 4번수행
n :5, 10번 수행
n :6, 20번수행
n :7, 35번수행
1,3,6,10,15

nCr : 서로 다른 n개에서 순서를 생각하지 않고 r개를 택하는 경우의 수.
nCr = n!/(n-r)!r! = nPr/r! = {n(n-1)(n-2)...(n-r+1)}/r!
'''
# import sys
# input = sys.stdin.readline
# print = sys.stdout.write

# N = int(input())
# arr = [int(input()) for _ in range(N)]
# arr.sort()
# print("\n".join(map(str, arr)))

# def recursion(s, l, r):
#     if l >= r: return 1
#     elif s[l] != s[r]: return 0
#     else: return recursion(s, l+1, r-1)

# def isPalindrome(s):
#     return recursion(s, 0, len(s)-1)


# N = int(input())
# for i in range(N):
#     s = input()
#     cnt = 1
#     for j in range(len(s)//2):
#         if s[j]==s[len(s)-j-1]:cnt+=1
#         else:break
#     print(isPalindrome(s), cnt)

# import sys
# input = sys.stdin.readline

# N,K = map(int, input().split()) #N:참가하는 학생 수, K:한 방에 배정할 수 있는 학생 수

# result = 0
# arr = []
# arr2 = []
# for i in range(N):
#     S,Y = map(str, input().split()) #S:성별(여학생:0, 남학생:1), Y:학년
#     arr.append(S+Y)

# arr2 = list(set(arr))

# for i in arr2:
#     tmp = arr.count(i)
#     if tmp%K==0:
#         result+= tmp//K
#     else:
#         result+= tmp//K+1
# print(result)

# import sys
# input = sys.stdin.readline

# N = int(input())
# stack = [int(input()) for i in range(N)]

# result = 1
# tmp = stack[N-1]
# for i in range(N-2,-1,-1):
#     if tmp<stack[i]:
#         result+=1
#         tmp = stack[i]
# print(result)
    