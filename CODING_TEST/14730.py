N = int(input())

res = 0 
for _ in range(N):
    C,K = map(int ,input().split())
    res += C*K

print(res)