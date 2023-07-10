N = int(input())
K = int(input())

start =1
end = K
while start<=end:
    mid = (start+end)//2
    
    tmp = 0
    for i in range(1,N+1):
        tmp +=min(mid//i,N)
    
    if tmp>=K:
        end = mid-1
    else:
        start = mid+1

print(start)