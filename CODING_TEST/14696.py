import sys
input = sys.stdin.readline

N = int(input())

res = []
for _ in range(N):
    A = list(map(int, input().split()))[1:]
    B = list(map(int, input().split()))[1:]
    
    for i in range(4,0,-1):
        if A.count(i)>B.count(i):
            res.append("A")
            break
        elif A.count(i)<B.count(i):
            res.append("B")
            break
        if i==1:
            res.append("D")
    
print(*res,sep='\n')
