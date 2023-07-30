N,M = map(int, input().split())
li = sorted(map(int, input().split()))

res = []
def dfs(x):
    if len(res)==M:
        print(*res,sep=' ')
        return
    for i in range(x,N):
        if li[i] in res:
            continue
        res.append(li[i])
        dfs(i+1)
        res.pop()

dfs(0)