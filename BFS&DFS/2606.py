from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

pc = [[0]*(N+1) for _ in range(N+1)]

for i in range(M):
    a,b = map(int, input().split())
    pc[a][b] = 1
    pc[b][a] = 1

visited = [0 for _ in range(N+1)]


def bfs(V):
    q = deque([V])
    visited[V] =1
    while q:
        V = q.popleft()
        for i in range(1, N+1):
            if not visited[i] and pc[V][i]:
                q.append(i)
                visited[i]=1

def dfs(V):
    visited[V] = 1
    for i in range(1,N+1):
        if not visited[i] and pc[V][i]:
            dfs(i)

dfs(1)
print(visited.count(1)-1)