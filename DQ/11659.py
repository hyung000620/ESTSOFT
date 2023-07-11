import sys
input = sys.stdin.readline

N,M = map(int, input().split())
li = list(map(int, input().split()))
for i in range(N-1):
    li[i+1] += li[i]
li.insert(0,0)
res = []
for i in range(M):
    s,e = map(int, input().split())
    res.append(li[e]-li[s-1])
    

print(*res,sep='\n')
