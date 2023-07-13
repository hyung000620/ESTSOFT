import sys
input = sys.stdin.readline

N = int(input())

res = dict()
for i in range(N):
    ext = (input().rstrip().split("."))[1]
    if not ext in res:
        res[ext] = 1
    else:
        res[ext] += 1
    
res = sorted(res.items())
for k, v in res:
    print(k,v)