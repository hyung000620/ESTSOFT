N,K = map(int, input().split())
A = list(map(int, input().split(",")))

B=[]
for _ in range(K):
    for i in range(len(A)-1):
        B.append(A[i+1]-A[i])    
    A,B=B,[]

print(*A,sep=',')
    