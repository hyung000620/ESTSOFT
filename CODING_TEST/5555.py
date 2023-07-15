s = input()
N = int(input())

cnt = 0
for _ in range(N):
    ring = input()
    
    if s in ring:
        cnt+=1
    else:
        for r in range(len(ring)):
            ring = ring[1:]+ring[0]
            if s in ring:
                cnt+=1
                break

print(cnt)