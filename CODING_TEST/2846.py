N = int(input())
Pi = list(map(int, input().split()))

res = []
tmp = 0
for i in range(1,N):
    if Pi[i]>Pi[i-1]:
        tmp += Pi[i]-Pi[i-1]
        res.append(tmp)
    else:
        res.append(tmp)
        tmp = 0

print(max(res))