import sys
from itertools import combinations
input = sys.stdin.readline

N,M = map(int, input().split())
like = [list(map(int, input().split())) for _ in range(N)]

maxSum = 0
for a, b, c in combinations(range(M), 3):
    tmpSum = 0
    for i in range(N):
        tmpSum += max(like[i][a], like[i][b], like[i][c])
    maxSum = max(maxSum, tmpSum)

print(maxSum)