import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    W,N = map(int,input().split())
    
    tcase = []
    for _ in range(N):
        x_i,w_i = map(int,input().split())
        tcase.append([x_i,w_i])
    c=d=v=0
    
    for i in tcase:
        if c + i[1] < W:
            d += i[0]-v
            c += i[1]
        elif c + i[1] == W:
            d += (i[0]-v) + i[0]*2
            c = 0
            if tcase.index(i) == N-1:
                d -= i[0]*2
        elif c + i[1] > W:
            c = i[1]
            d += (i[0] - v) + i[0]*2
        v = i[0]
    if tcase.index(i) == N-1:
        d += i[0]
    print(d)
    
    
    
        
