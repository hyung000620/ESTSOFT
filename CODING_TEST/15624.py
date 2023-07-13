N = int(input())

dp = [0]*1000001
dp[0]=0
dp[1]=1
dp[2]=1


for i in range(3,N+1):
    dp[i]=(dp[i-1]+dp[i-2])%1000000007

print(dp[N])

