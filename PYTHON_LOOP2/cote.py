# N = int(input())
# print(' '*(N-1) +'*')
# for i in range(N-1):
#     print(" "*(N-2-i)+"*"+" "*(2*i+1)+"*")

# n = int(input())
# print(" "*(n-1)+"*")
# if n !=1:
#     for i in range(1,n-1):
#         print(" "*(n-1-i)+"*"+" "*(2*i-1)+"*")
#     print("*"*(2*n-1))

# n = int(input())

# for _ in range(n):
#     print('* '* (n - n//2))
#     print(' *'* (n//2))

# n = int(input())

# for i in range(2*n-1):
#     print("*")


# k = int(input())-1

# q=[input().split() for _ in range(int(input()))]

# result=0 
# for time,compare in q: 
#     result += int(time) 
#     if result >= 210: 
#         print(k+1) 
#         break 
#     if compare =='T': 
#         k = (k+1)%8
# a = {'1':1,'3':1,'2':1}
# c =[]

# for v in a.values():
#     c += [v]

# print(c)

# gangsa = [{"이름": "김도언", "나이": 20, "직업": "강사", "일일퀴즈성적": [10, 20, 20]},
# {"이름": "이예원", "나이": 21, "직업": "멘토", "일일퀴즈성적": [9, 19, 19]}]

# ganga_add_info = {"회사": "이스트소프트", "강의기수":"2기"}

# for i in gangsa:
#     i['일일퀴즈성적'].append(30)

# print(gangsa)
# import sys
# input = sys.stdin.readline

# n,k = map(int, input().split())
# arr = list(map(int, input().split()))
# arr.sort(reverse=True)

# print(arr[k-1])

# import sys
# input = sys.stdin.readline

# line = []
# k = int(input())
# numbers = list(map(int, input().split()))
# for i in range(k):
#     line.insert(numbers[i],i+1)

# print(*line[::-1])

# a,b = input().split()
# print(int(a, int(b)))

# N,M=map(int, input().split())
# arr=[a+1 for a in range(N)]

# for t in range(M):
#     i,j = map(int, input().split())
#     arr = arr[:i-1]+arr[i-1:j][::-1]+arr[j:]

# print(*arr)

# arr=[int(input()) for i in range(10)]
# avg = sum(arr)//10

# print(avg)
# max_num=0
# tmp = 0
# for a in arr:
#     if tmp < arr.count(a):
#         tmp = arr.count(a)
#         max_num = azss
# print(max_num)

# T = int(input())

# for i in range(T):
#     arr = list(map(str, input().split()))
#     num = float(arr[0])
#     for j in arr[1:]:
#         if j == '@':num*=3
#         elif j=='%':num+=5
#         else: num-=7
#     print(f"{num:.2f}")

# x,y=map(int,input().split()) # x월 y일 에 요일 구하기

# week=["MON","TUE","WED","THU","FRI","SAT","SUN"] # 요일 list
# date={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31} #월별 일수 dict
# c=0
# for i in range(1,x):
#     c+= date[i]
# c+=y
# c%=7
# print(week[c])

# arr = [int(input()) for _ in range(20)]
# w_arr = arr[:10]
# k_arr = arr[10:]
# w_arr.sort(reverse=True)
# k_arr.sort(reverse=True)
# print(f"{sum(w_arr[:3])} {sum(k_arr[:3])}")

#5
'''
첫째 줄에는 별 1개, 둘째 줄에는 별 3개, ..., N번째 줄에는 별 (2 X N-1)개를 찍는 문제
'''

#오늘 배운 list 합치는거 응용하였습니다.
# n = int(input())
# for i in range(n,0,-1):
#     print(' '* (n-i)+'*'* (2*i-1))
# for i in range(2,n+1):
#     print(' ' * (n-i) + '*' * (2*i-1))

# matrix = [[1,5,7],[2,4,6]]


# print(matrix[1][1])

# n=int(input())
# for i in range(1,n+1):
#     print("*"*(i)+" "*(n-i))
# for i in range(1,n):
#     print("*"*(n-i)+" "*i)
    
# a=int(input())
# for i in range(1,a+1):
#     print('*'*i)
# for i in range(1,a):
#     print('*'*(a-i))