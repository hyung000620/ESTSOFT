from collections import deque
from sys import stdin

input = stdin.readline
def main():
    n = int(input())
    queue = deque()
    res = []
    for _ in range(n):
        li = list(map(int,input().split()))
        
        cmd = li[0]
        if cmd == 1:
            queue.appendleft(li[1])
        elif cmd == 2:
            queue.append(li[1])
        elif cmd == 3:
            res.append(queue.popleft() if len(queue) else -1)
        elif cmd == 4:
            res.append(queue.pop() if len(queue) else -1)
        elif cmd == 5:
            res.append(len(queue))
        elif cmd == 6:
            res.append(0 if len(queue) else 1)
        elif cmd == 7:
            res.append(queue[0] if len(queue) else -1)
        elif cmd == 8:
            res.append(queue[-1] if len(queue) else -1)
        
    print(*res, sep='\n')

if __name__ == "__main__":
    main()