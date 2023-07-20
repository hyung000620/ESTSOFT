cow = [2]*11
N = int(input())

cnt =0
for i in range(N):
    num,position = map(int, input().split())
    
    if cow[num]==2:
        cow[num]=position    
    elif cow[num]!=position:
        cnt+=1
        cow[num]=position

print(cnt)
