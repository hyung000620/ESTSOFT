N,M = map(int, input().split())

A = set(map(int,input().split()))
B = set(map(int,input().split()))

res = sorted(A-B)

if len(res):
    print(len(res))
    print(*res, sep=' ')
else:
    print(len(res))