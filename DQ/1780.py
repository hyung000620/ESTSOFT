import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int,input().split())) for _ in range(N)]

res = {-1:0,0:0,1:0}
def sol(x,y,N):
    color = paper[x][y]
    for i in range(x,x+N):
        for j in range(y,y+N):
            if color!= paper[i][j]:
                for k in range(3):
                    for l in range(3):
                        sol(x+N//3*k, y+N//3*l, N//3)
                return
    
    res[color]+=1
    return 
    
sol(0,0,N)
for i in res.values():
    print(i)

                