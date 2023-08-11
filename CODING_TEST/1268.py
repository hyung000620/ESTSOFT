import sys
input = sys.stdin.readline

n = int(input())

ban = []
same =[0]*n
for i in range(n):
    ban.append(list(map(int,input().split())))
    same[i] = [0]*n

for i in range(5):
    for j in range(n):
        for k in range(j+1,n):
            if ban[j][i] == ban[k][i]:
                same[k][j] =1
                same[j][k] =1

res = []
for s in same:
    res.append(s.count(1))
print(res.index(max(res))+1)