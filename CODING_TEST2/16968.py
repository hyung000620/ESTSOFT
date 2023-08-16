S = input()
N = len(S)

res = 26 if S[0]=='c' else 10
for i in range(1,N):
    if S[i] == 'd':
        if S[i-1] == 'd': res*=9
        else:res *=10
    else:
        if S[i-1] == 'c': res*=25
        else:res *=26

print(res)