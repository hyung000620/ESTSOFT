n,k = map(int, input().split())
arr = [[1]*(i+1) for i in range(n)]

for i in range(2,n):
    for j in range(1,len(arr[i])):
        arr[i][j]=sum(arr[i-1][j-1:j+1])

print(arr[n-1][k-1])