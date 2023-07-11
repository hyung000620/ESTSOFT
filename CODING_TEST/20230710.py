# 일일 복습문제
import sys
input = sys.stdin.readline
N,M = map(int, input().split())
li = list(map(int, input().split()))

start = max(li)
end = sum(li)
while start <= end:
    mid = (start+end)//2
    cnt = 1
    tmp = 0
    for i in li:
        if tmp+i>mid:
            cnt+=1
            tmp = 0
        tmp+=i
    
    if cnt<=M:
        end = mid-1
    else:
        start = mid+1
        
print(start)

# N, M = map(int, input().split())
# dduk = list(map(int,input().split()))

# start = 0
# end = max(dduk)

# while start<=end:
#     mid = (start+end)//2
    
#     tmp = 0
#     for i in dduk:
#         if i>mid:
#             tmp +=i-mid
    
#     if tmp<M:
#         end = mid -1
#     else:
#         start = mid +1

# print(end)