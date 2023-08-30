from sys import stdin
input = stdin.readline

n = int(input())
stack = []
res = []
for i in range(n):
    li = list(map(int, input().split()))
    
    cmd = li[0]
    if cmd == 1:
        stack.append(li[1]) 
    elif cmd == 2:
        res.append(stack.pop() if len(stack) else -1)
    elif cmd == 3:
        res.append(len(stack))
    elif cmd == 4:
        res.append(0 if len(stack) else 1)
    elif cmd == 5:
        res.append(stack[-1] if len(stack) else -1)
        

print(*res, sep='\n')