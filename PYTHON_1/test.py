# #1
# print(len(input()))

# #2
# y,m,d=input().split("-")

# print(f"연도: {y}")
# print(f"월: {m}")
# print(f"일: {d}")

# #3
# a = int(input())
# print(f"몫: {a//2}")
# print(f"나머지: {a%2}")

# #4
# c = int(input())
# print(int(c*9/5+32))


# #5
# file_path = input("파일 이름을 입력하세요:")
# file_context = input("파일 내용을 입력하세요:")

# with open(file_path,"w") as f:f.write(file_context)
# print("파일 생성 및 내용 저장이 완료되었습니다.")
# print("파일을 열어 내용을 확인하는 동물이 있습니다...")
# print(f"고양이가 {file_path} 파일을 열어 아래 내용을 확인합니다.")
# with open(file_path,"r") as f :context = f.read()

# print(f"파일 내용: {context}")

# print("10**2+3*5") 

# A, B = [], []

# N, M = map(int, input().split())
# i=0
# for row in range(N*2):
#     row = list(map(int, input().split()))
#     if i<N : A.append(row)
#     else: B.append(row)
#     i +=1
  
# for row in range(N):
#     for col in range(M):
#         print(A[row][col] + B[row][col], end=' ')
#     print()

# s_dict = {"NLCS": "North London Collegiate School"
# ,"BHA": "Branksome Hall Asia"
# ,"KIS": "Korea International School"
# ,"SJA": "St. Johnsbury Academy"}

# print(s_dict[input()])

# n, a, b = map(int, input().split())
# if a < b: print('Bus')
# elif a > b: print('Subway')
# else: print('Anything')

# s_dict = {
#     "SONGDO":"HIGHSCHOOL",
#     "CODE":"MASTER",
#     "2023":"0611",
#     "ALGORITHM":"CONTEST"
# }

# print(s_dict[input()])

# while True:
#     cnt = 0
#     i = input().upper()
#     if i == "#": break
#     for c in i: 
#         if c in 'AEIOU': cnt+=1
#     print(cnt)

# N, M = map(int, input().split())
# for _ in range(N):
#     print(input()[::-1])

# N = int(input())
# i = 1
# for _ in range(N):
#     print(f"{i}. {input()}")
#     i +=1

# N = int(input())
# for _ in range(N):
#     print(input().lower())

# N = int(input()) # 치킨 수
# A,B = map(int, input().split()) #콜라, 맥주 개수

# A = A//2
# if N <= A+B : print(N)
# else: print(A+B)

# print("Naver D2" if input().upper() == "N" else "Naver Whale")

# N = int(input()) #가게의 수
# i = 0
# time = 0
# for _ in range(N):
#     A,B = map(int, input().split())
#     if B>=A:
#         time += B-A
#     if i == N: time = -1
#     i+=1
# print(time)

# mbti = input()
# N = int(input())
# cnt = 0
# for _ in range(N):
#     if input() == mbti: cnt+=1
# print(cnt)

# A,B = map(int,input().split())
# A //=2
# if A<B : print(A)
# else : print(B)

# N = int(input())
# cnt=0
# for _ in range(N):
#     day = input().split("-")[1]
#     if int(day) <=90 : cnt +=1
# print(cnt)

# x,y = map(int, input().split())

# if x>y : print(x+y)
# else: print(y-x)

# n = input()
# a = len(n)
# b,c = 0,0
# for i in range(a):
#     if n[i] ==":":b+=1
#     elif n[i] == "_":c+=1
# c *=5
# print(a+b+c)

for i in range(5):
    print(i)