import sys
input = sys.stdin.readline

n = int(input())

rope = [int(input()) for _ in range(n)]
rope.sort(reverse=True)
res = []
for i in range(n):
    res.append(rope[i]*(i+1))
    
print(max(res))