N = int(input())

res = []
def dfs(x):
    if len(res) == N:
        print(*res, sep=' ')
        return
    for i in range(1,N+1):
        if i in res:
            continue
        res.append(i)
        dfs(x+1)
        res.pop()    

dfs(1)