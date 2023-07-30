N,M = map(int, input().split())
li = sorted(map(int, input().split()))

res = []

def dfs(x):
    if len(res) == M:
        print(*res,sep=' ')
        return
    for i in range(x,N):
        res.append(li[i])
        dfs(i)
        res.pop()

dfs(0)