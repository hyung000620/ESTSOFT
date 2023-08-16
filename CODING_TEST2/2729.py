from sys import stdin
input = stdin.readline

T = int(input())

res = []
for _ in range(T):
    a,b = map(lambda x : int("0b"+x,2) ,input().rstrip().split())
    
    res.append(bin(a+b)[2:])

print(*res,sep='\n')