import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))

dp1 = [1]*n
dp2 = [1]*n
for i in range(n):
    for j in range(i):
        if a[j]<a[i]:
            dp1[i] = max(dp1[i],dp1[j]+1)

for i in range(n-1,-1,-1):
    for j in range(n-1,i,-1):
        if a[j]<a[i]:
            dp2[i] = max(dp2[i],dp2[j]+1)

dp = [0]*n
for i in range(n):
    dp[i] = dp1[i]+dp2[i]-1

print(max(dp))
        