# 속도 테스트. 내가 쓴거 아님
def bfs(queue):
    while queue:
        i, j = queue.pop(0)
        for di, dj in delta:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and not space[ni][nj]:
                queue.append((ni, nj))
                space[ni][nj] = space[i][j] + 1


n, m = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(n)]

delta = ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1))
queue = []
for i in range(n):
    for j in range(m):
        if space[i][j]:
            queue.append((i, j))

bfs(queue)
print(max(sum(space, [])) - 1)