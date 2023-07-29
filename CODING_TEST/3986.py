import sys
input = sys.stdin.readline

N = int(input())

cnt = 0
for _ in range(N):
    ab = input().rstrip()
    li = []
    for i in ab:
        if li:
            if i == li[-1]:
                li.pop()
            else:
                li.append(i)
        else:
            li.append(i)    
    if not li:
        cnt+=1

print(cnt)