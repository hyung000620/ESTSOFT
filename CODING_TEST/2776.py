import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    arr1 = set(map(int, input().split()))
    M = int(input())
    arr2 = list(map(int, input().split()))
    for i in arr2:
        if i in arr1:
            print(1)
        else:
            print(0)