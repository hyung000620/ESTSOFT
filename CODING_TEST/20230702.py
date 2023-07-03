# n = int(input())

# trophy = [int(input()) for i in range(n)]

# left = right = 0
# left_max = right_max = 0

# for n in trophy:
#     if n > left_max:
#         left_max = n
#         left += 1
# for n in trophy[::-1]:
#     if n > right_max:
#         right_max = n
#         right += 1
        
# print(left)
# print(right)

# n = input()

# if int(n[0]):
#     print(int(n))
# elif n[1]=="x":
#     print(int(n,16))
# else:
#     print(int(n,8))
'''
영식이가 운동을 하는 과정은 1분 단위로 나누어져 있다. 매 분마다 영식이는 운동과 휴식 중 하나를 선택해야 한다.
운동을 선택한 경우, 영식이의 맥박이 T만큼 증가한다. 즉, 영식이의 맥박이 X였다면, 1분 동안 운동을 한 후 맥박이 X+T가 되는 것이다.
영식이는 맥박이 M을 넘는 것을 원하지 않기 때문에, X+T가 M보다 작거나 같을 때만 운동을 할 수 있다. 휴식을 선택하는 경우 맥박이 R만큼 감소한다.
즉, 영식이의 맥박이 X였다면, 1분 동안 휴식을 한 후 맥박은 X-R이 된다. 맥박은 절대로 m보다 낮아지면 안된다.
따라서, X-R이 m보다 작으면 맥박은 m이 된다.
영식이의 초기 맥박은 m이다. 운동을 N분 하려고 한다. 이때 운동을 N분하는데 필요한 시간의 최솟값을 구해보자. 운동하는 시간은 연속되지 않아도 된다.
'''
# N, m, M, T, R = map(int, input().split())
# X=m
# time = cnt =  0

# while cnt<N:
#     if m+T>M:break
    
#     if X +T<=M:
#         X+=T
#         cnt+=1
#     else:
#         X = max(X-R,m)
#     time+=1
    
    
# print(time if cnt==N else -1)

#27433
# ||
# ```py
# def factorial(n):
#     return n*factorial(n-1) if n else 1

# print(factorial(int(input())))
# ```
# ||
#10870
# ||
# ```py
# def fibonachi(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonachi(n-2)+fibonachi(n-1)


# print(fibonachi(int(input())))
# ```
# ||

# ||
# ```py
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
# ```
# ||


# apartments = [{"세대": 2301, "이름": "종민아파트"}, {"세대":1500, "이름": "은철아파트"}, {"세대": 3999, "이름": "지수아파트"}]

# apartments.sort(key=lambda x: x['세대'])

# print(apartments)


class Car:
    def  __init__(self, model, car_type="electric"):
          self.model = model
          self.wheel = 4
          self.speed = 50
          self.car_type = car_type
    def brake(self):
          self.speed -= 50
    def accelerate(self):
          self.speed += 50

my_car = Car("Tesla")
my_car.accelerate()
my_car.accelerate()
my_car.brake()
print(my_car.model, my_car.wheel, my_car.speed)