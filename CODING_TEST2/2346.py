from collections import deque
from sys import stdin

input = stdin.readline
queue = deque()

n = int(input())
bomb = list(map(int, input().split()))
pungsuns = [i for i in range(1, n+1)]

