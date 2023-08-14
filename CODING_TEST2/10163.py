import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
queries, line_x, line_y = [], set(), set()

for _ in range(N):
	q = list(map(int, input().split()))
	x1, y1, x2, y2 = q[0], q[1], q[0] + q[2], q[1] + q[3]
	queries.append((x1, y1, x2, y2))
	line_x.add(x1)
	line_x.add(x2)
	line_y.add(y1)
	line_y.add(y2)

line_x = sorted(line_x)
line_y = sorted(line_y)
comp_x = {v: i for i, v in enumerate(line_x)}
comp_y = {v: i for i, v in enumerate(line_y)}
dx = [line_x[i] - line_x[i - 1] for i in range(1, len(line_x))]
dy = [line_y[i] - line_y[i - 1] for i in range(1, len(line_y))]

paper = [[0] * len(dx) for _ in range(len(dy))]

for i in range(1, len(queries) + 1):
	x1, y1, x2, y2 = queries[i - 1]
	for x in range(comp_x[x1], comp_x[x2]):
		for y in range(comp_y[y1], comp_y[y2]):
			paper[y][x] = i

ans = [0] * (N + 1)
for y in range(len(paper)):
	for x in range(len(paper[0])):
		ans[paper[y][x]] += dx[x] * dy[y]

print('\n'.join(map(str, ans[1:])))