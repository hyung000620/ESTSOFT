import sys
input = sys.stdin.readline

N = int(input())

time = []
for i in range(N):
    start,end = map(int,input().split())
    time.append([start,end])

time.sort(key=lambda x: x[0])
time.sort(key=lambda x: x[1])
    
time.sort(key=lambda x: (x[1],x[0]))

cnt, end = 0,0
for s,e in time:
    if s>=end:
        cnt+=1
        end=e
print(cnt)