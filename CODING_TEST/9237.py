N = int(input())

tree = sorted(map(int, input().split()),reverse=True)

for i in range(N):
    tree[i] = tree[i]+i+1

print(max(tree)+1)