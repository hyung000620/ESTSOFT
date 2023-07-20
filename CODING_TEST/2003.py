N,M = map(int, input().split())
li = list(map(int, input().split()))

cnt, left, right = 0,0,1

while right<=N and left<=right:
    
    hap = sum(li[left:right])
    
    if hap == M:
        cnt+=1
        right+=1
    elif hap<M:
        right+=1
    else:
        left+=1

print(cnt)