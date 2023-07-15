N,M = map(int ,input().split())

jpg = [[0]*101 for _ in range(101)]

for _ in range(N):
    x1,y1,x2,y2 = map(int, input().split())
    
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            jpg[i][j]+=1

cnt = 0
for i in jpg:
    for j in i:
        if j>M:
            cnt+=1

print(cnt)