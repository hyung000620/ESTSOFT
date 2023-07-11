import sys
input = sys.stdin.readline

dp = [0]*101
dp[1]=1
dp[2]=1
dp[3]=1
T = int(input())
for i in range(T):
    N = int(input())
    
    for i in range(4,N+1):
        dp[i] = dp[i-2]+dp[i-3]
    
    print(dp[N])