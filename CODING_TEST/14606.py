N = int(input())
# dp = [0]*11
# dp[1]=0
# dp[2]=1
# dp[3]=3
# for i in range(4,N+1):
#     m = i//2
#     dp[i] = m*(i-m)+dp[m]+dp[i-m]

# print(dp)
dp = [0, 0, 1, 3, 6, 10, 15, 21, 28, 36, 45]
print(dp[N])