A,B = map(int, input().split())
N = int(input())

cnt = abs(A-B)
for _ in range(N):
    btn = int(input())

    cnt = min(abs(btn-B)+1,cnt)

print(cnt)