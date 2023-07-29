import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

res = []
for _ in range(T):
    M, M = map(int, input().split())
    q = deque(list(map(int, input().split())))
    
    cnt = 0
    while q:
        max_val = max(q)
        front = q.popleft()
        M -=1
        
        if max_val == front:
           cnt+=1
           if M<0:
               res.append(cnt)
               break
        else:
            q.append(front)
            if M<0:
                M = len(q)-1

print(*res,sep='\n')
        