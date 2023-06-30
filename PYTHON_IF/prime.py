# from itertools import combinations

# # 소수를 구하는 함수
# def is_prime(n):
#     if n < 2:
#         return False
#     # 주어진 수의 제곱근 까지만 나누어떨어지지 않아도 소수 판별 가능
#     for i in range(2, int(n ** 0.5) + 1): # n의 0.5승 = 루트n
#         if n % i == 0:
#             return False
#     return True

# def solution(nums):
#     answer = 0
#     for num in combinations(nums, 3):
#         if is_prime(sum(num)) == True:
#             answer += 1
    
#     return answer

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(arr[0],arr[-1])