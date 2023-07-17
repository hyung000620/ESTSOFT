N = int(input())
Pi = list(map(int, input().split()))

res = []
tmp = 0
for i in Pi:
    if i>tmp:
        tmp = i
        res.append(tmp)
    elif i<tmp:
        tmp = 0
        res.clear()