import sys
input = sys.stdin.readline

K,N = map(int,input().split())
lan = [int(input()) for i in range(K)]

start, end = 1, max(lan)

while start<=end:
    mid = (start+end)//2
    total = 0
    
    total = sum(list(map(lambda x: x//mid,lan)))
    
    if total < N:
        end = mid-1
    else:
        start = mid+1
        
print(end)