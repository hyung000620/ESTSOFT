import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

dp = [1]*n
for i in range(1,n):
    for j in range(i):
        if arr[i]>arr[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))

x = max(dp)
res = []
for i in range(n-1,-1,-1):
    if dp[i]==x:
        res.append(arr[i]) 
        x-=1

print(*res[::-1],sep=" ")

