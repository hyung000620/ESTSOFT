import sys
input = sys.stdin.readline

N,M = map(int,input().split())
times = [int(input()) for _ in range(N)]

start,end = 1, max(times)*M
while start<=end:
    mid = (start+end)//2
    people = 0
    for t in times:
        people += mid//t
        
    if people>=M:
        end = mid -1
    else:
        start = mid+1
        
print(start)

#start 최솟값, end 최댓값
