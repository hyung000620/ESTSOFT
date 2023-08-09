L = int(input())
N = int(input())

cake = [0]*(L+1)
received = [0]*(N+1)
real,want = 0,0

for i in range(1,N+1):
    cnt = 0
    P,K = map(int, input().split())
    
    tmp = K-P
    if real < tmp:
        real = tmp
        want = i
    
    for j in range(P,K+1):
        if cake[j] == 0:
            cake[j] = i
            cnt +=1
    received[i] = cnt

print(want)
print(received.index(max(received)))