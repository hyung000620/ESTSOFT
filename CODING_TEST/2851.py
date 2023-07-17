import sys
input = sys.stdin.readline

m = [int(input()) for _ in range(10)]
score = 0

for j in m:
    score += j
    if score >= 100:
        if score - 100 > 100 - (score - j):
            score -= j
        break
print(score)