N,M = map(int, input().split())

ans1 = [0]*N
ans2 = [0]*M
for i in range(N):
    li = input()
    if 'X' in li:
        ans1[i]=1
    for j in range(M):
        if li[j]=='X':
            ans2[j]=1

res = 0
if ans1.count(0)>ans2.count(0):
    res = ans1.count(0)
else:
    res = ans2.count(0)

print(res)