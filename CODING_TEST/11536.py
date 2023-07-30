import sys
input = sys.stdin.readline

N = int(input())

name = [input().rstrip() for _ in range(N)]
inc = sorted(name)
dec = sorted(name,reverse=True)

if name == inc:
    print("INCREASING")
elif name == dec:
    print("DECREASING")
else:
    print("NEITHER")