import sys
input = sys.stdin.readline

N,M = map(int, input().split())
tree = list(map(int, input().split()))

start,end = 1, max(tree)
while start<=end:
    mid = (start+end)//2
    h = 0
    for i in tree:
        if i-mid>0:
            h += i-mid
    if h<M:
        end = mid-1
    else:
        start = mid+1
print(end)