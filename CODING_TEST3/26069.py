from sys import stdin
from collections import defaultdict
input = stdin.readline

n = int(input())
dance = defaultdict(bool)
dance['ChongChong'] = True

for _ in range(n):
    a,b = input().rstrip().split()
    if dance[a] or dance[b]:
        dance[a] = dance[b] = True
        
true_count = sum(1 for value in dance.values() if value)
print(true_count)