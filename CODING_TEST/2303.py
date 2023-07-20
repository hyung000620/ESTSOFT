import sys
input = sys.stdin.readline

N = int(input())

li = [0]*N

for idx in range(N):
    arr = list(map(int, input().split()))
    
    tmp = 0
    for i in range(5):
        for j in range(i+1,5):
            for k in range(j+1,5):
                tmp = max((arr[i]+arr[j]+arr[k])%10,tmp)
    
    li[idx]=tmp

for i in range(N - 1, -1, -1):
  if li[i] == max(li): 
    print(i + 1)
    break
