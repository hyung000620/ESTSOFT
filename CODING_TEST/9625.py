K = int(input())
A,B=0,1
for i in range(1,K):
    A,B = B,A+B

print(A,B)