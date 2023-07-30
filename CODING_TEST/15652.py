N,M = map(int, input().split())

li = []
def dfs(x):
    if len(li) ==M:
        print(' '.join(map(str,li)));
        return
    for i in range(x,N+1):
        li.append(i)
        dfs(i)
        li.pop()

dfs(1)