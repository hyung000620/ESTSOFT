import sys
input = sys.stdin.readline

def dfs(idx,cnt):
    visited[idx] = 1
    

T = int(input())

for _ in range(T):
    N,M = map(int, input().split())
    visited = [False]*(N+1)
    
    for i in range(M):
        start,end = map(int,input().split())
