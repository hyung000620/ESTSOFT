# import sys
# input = sys.stdin.readline

# n = int(input())
# rgb = [list(map(int,input().split())) for _ in range(n)]

# dp = [0]*n

# res = 0
# for i in range(n):
#     dp[i]=rgb[i][0]
#     for j in range(n):
#         dp[i] = min(rgb[j][i],dp[i])

# print(sum(dp))
