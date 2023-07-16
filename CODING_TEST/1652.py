N = int(input())
position = [input() for _ in range(N)]

garo, sero = 0,0

for i in range(N):
    gcnt = scnt=0
    for j in range(N):
        if position[i][j] == ".":
            gcnt+=1
        else:
            gcnt= 0
        if gcnt==2:
            garo+=1
            
        if position[j][i] == ".":
            scnt +=1
        else:
            scnt=0
        if scnt==2:
            sero+=1
            
        

print(garo, sero)