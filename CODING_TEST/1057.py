N,K,L = map(int, input().split())

cnt = 0
while K!=L:
    K -= K//2
    L -= L//2
    cnt+=1
print(cnt)