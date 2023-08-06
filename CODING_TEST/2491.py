import sys
input = sys.stdin.readline

def search(arr,N):
    dp = [0]*N
    dp[0]=1
    for i in range(1,N):
        if arr[i]>=arr[i-1]:
            dp[i]=dp[i-1]+1
        else:
            dp[i]=1
    
    return max(dp)

N = int(input())
li = list(map(int, input().split()))

max1 = search(li,N)
li.reverse()
max2 = search(li,N)

print(max(max1, max2))