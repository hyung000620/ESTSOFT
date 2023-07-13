import sys
input = sys.stdin.readline
print = sys.stdout.write

M = int(input())
S = set()
for i in range(M):
    li = input().rstrip().split()
    cmd = li[0]
    
    match cmd:
        case "add":
            S.add(int(li[1]))    
        case "check":
            print('1\n') if int(li[1]) in S else print('0\n')
        case "remove":
            S.discard(int(li[1]))
        case "toggle":
            S.discard(int(li[1])) if int(li[1]) in S else S.add(int(li[1]))
        case "all":
            S.update([i for i in range(1,21)])
        case "empty":
            S.clear()