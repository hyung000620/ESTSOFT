import sys
input = sys.stdin.readline

N = int(input())

milk = [int(input()) for _ in range(N)]

milk.sort(reverse=True)
res = 0
for i in range(N):
    if i%3!=2:
        res+= milk[i]
print(res)