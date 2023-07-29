def koong(n):
    dp = [0]*68
    dp[0]=1
    dp[1]=1
    dp[2]=2
    dp[3]=4
    for i in range(4,n+1):
        dp[i]=dp[i-1]+dp[i-2]+dp[i-3]+dp[i-4]
    return dp[n]

t = int(input())
li = []
for i in range(t):
    N = int(input())
    li.append(koong(N))

print(*li,sep='\n')