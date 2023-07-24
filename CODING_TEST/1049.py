N,M = map(int,input().split())

ans = 0
p_list = []
s_list = []
for i in range(M):
    p, s = map(int,input().split())
    p_list.append(p)
    s_list.append(s)

p = min(p_list)
s = min(s_list)

ans1 = (N//6*p)+(N%6*s)
ans2 = (N//6+1)*p
ans3 = N*s

ans = min(ans3,min(ans1,ans2))
print(ans)