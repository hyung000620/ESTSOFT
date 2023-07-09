# import re

# text = "Hello, SeongGi. This is my password 125@1"
# pattern = r'\d{2,}|@'

# for i in re.findall(pattern, text):
#      try:
#           print(int(i))
#      except:
#           print("숫자가 아닙니다.")

# class Animal:
#     def speak(self):
#         print("동물이 소리를 냅니다.")

# class Dog(Animal):
#     def speak(self):
#         # super().speak()
#         print("개가 짖습니다.")


# d1 = Dog()
# d1.speak()

# import sys
# input = sys.stdin.readline

# def gcd(a,b):
#     while b>0:
#         a,b=b,a%b
#     return a

# n = int(input())
# first = int(input())

# li = []
# for i in range(n-1):
#     tree = int(input())
#     li.append(tree-first)
#     first = tree

# g = li[0]
# for i in range(1, len(li)):
#     g = gcd(g, li[i])

# res = 0
# for i in li:
#     res += i//g -1
# print(res)

# import sys
# input = sys.stdin.readline

# def prime(a):
#     for i in range(2,int(a**0.5)+1):
#         if a%i==0:
#             return False
#     return True
        
# n = int(input())
# for i in range(n):
#     num = int(input())
#     while True:
#         if num in [0,1]:print(2);break
#         elif prime(num):print(num);break
#         num+=1

# import sys
# input = sys.stdin.readline

# N,L = map(int, input().split())

# fruits = sorted(map(int,input().split()))

# for f in fruits:
#     if f<=L:
#         L+=1
        
# print(L)