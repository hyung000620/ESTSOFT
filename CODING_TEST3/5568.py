from sys import stdin
from itertools import permutations
input = stdin.readline

n = int(input())
k = int(input())

cards = [input().rstrip() for _ in range(n)]

res = set()
for p in permutations(cards, k):
    res.add(''.join(p))
    
print(len(res))