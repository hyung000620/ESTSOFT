a,b = map(int, input().split())
m = int(input())
li = list(map(int, input().split()))

li.reverse()

ten = 0
for i in range(m):
    ten += li[i]*(a**i)

res = []
while ten>0:
    res.append(ten%b)
    ten //=b

print(*res[::-1])
    