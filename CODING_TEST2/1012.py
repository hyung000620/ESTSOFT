"""
실버 2 유기농 배추
BFS 알고리즘으로 문제를 해결하였습니다.
1인 값이 있으면 상,하,좌,우, 값도 1로 바꿔주고
cnt 값을 1로 증가시키는 방식을 사용하였습니다.
"""
import sys
input = sys.stdin.readline

T = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = [(x,y)]
    bat[x][y]=0
    
    while queue:
        x,y = queue.pop(0)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            
            if bat[nx][ny] == 1:
                queue.append((nx,ny))
                bat[nx][ny] = 0
    


res = []
for _ in range(T):
    M,N,K = map(int, input().split())
    bat = [[0]*N for _ in range(M)]
    cnt = 0
    
    for _ in range(K):
        x,y = map(int, input().split())
        bat[x][y]=1
    
    for a in range(M):
        for b in range(N):
            if bat[a][b] == 1:
                bfs(a,b)
                cnt +=1
                
    res.append(cnt)
    
print(*res,sep='\n')
    