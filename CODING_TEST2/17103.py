from sys import stdin
input = stdin.readline

arr = [True for _ in range(1000001)]
for i in range(2,1001):
    if arr[i]:
        for j in range(i + i , 1000001, i):
            arr[j] = False

T = int(input())
res = []
for _ in range(T):
    n = int(input())
    cnt = 0
    for i in range(2, n//2+1):
        if arr[i] and arr[n-i]:
            cnt += 1
    res.append(cnt)

print(*res, sep='\n') 