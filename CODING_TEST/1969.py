N, M = map(int, input().split())

dna = [input() for _ in range(N)]


cnt = 0
res = ""
for i in range(M):
    t_dict = dict()
    for j in range(N):
        tmp = dna[j][i]
        if tmp in t_dict:
            t_dict[tmp] +=1
        else:
            t_dict[tmp] = 1
    li = sorted(t_dict.items(),key=lambda x: (-x[1],x[0]))
    res += li[0][0]
    cnt += N-li[0][1]

print(res)
print(cnt)