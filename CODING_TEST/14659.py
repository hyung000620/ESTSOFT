N = int(input())
arr = list(map(int, input().split()))

res,max_val, cnt = 0,0,0

for i in arr:
    if i>max_val:
        max_val = i
        cnt = 0
    else:
        cnt+=1
    res = max(res,cnt)
print(res)