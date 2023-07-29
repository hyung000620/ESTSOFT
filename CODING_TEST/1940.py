N = int(input())
M = int(input())

steel = sorted(map(int, input().split()))

cnt, left,right = 0,0,N-1

while left<right:
    tmp = steel[left] + steel[right];
    if tmp == M:
        cnt+=1
        left +=1
        right -=1
    elif tmp >M:
        right-=1
    else:
        left+=1
        
print(cnt)