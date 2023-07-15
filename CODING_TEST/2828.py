N,M = map(int, input().split())
J = int(input())

left, right = 1,M
cnt = 0
for _ in range(J):
    a = int(input())
    if a>right:
        cnt += (a-right)
        left +=(a-right)
        right = a
    elif a<left:
        cnt += (left-a)
        right -=(left-a)
        left =a
        
print(cnt)