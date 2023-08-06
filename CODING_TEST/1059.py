import sys
input = sys.stdin.readline

L = int(input())
S = list(map(int, input().split()))
n = int(input())

if n in S:
    print(0)
else:
    min_val = 0
    max_val = 1000
    for i in S:
        if i<n:min_val = max(min_val,i)
        else:max_val = min(max_val,i)
    
    cnt = 0
    for i in range(min_val+1,max_val-1):
        for j in range(i+1,max_val):
            if i <= n and j >= n:
                cnt += 1
    print(cnt)