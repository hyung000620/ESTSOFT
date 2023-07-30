N,M = map(int, input().split())
li = list(map(int, input().split()))

li.sort()
res = []
def dfs(x):
    if len(res)==M:
        print(*res,sep=' ')
        return
    for i in range(N):
        if li[i] in res:
            continue
        res.append(li[i])
        dfs(x+1)
        res.pop()        
    
dfs(0)