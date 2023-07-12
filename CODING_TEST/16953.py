import sys
input = sys.stdin.readline

A,B = map(int, input().split())

cnt = 1
while B!=A:
    cnt +=1
    tmp = B
    if B%2==0:
        B//=2
    elif B%10==1:
        B//=10
        
    if tmp == B:
        print(-1)
        break
else:
    print(cnt)
    
            