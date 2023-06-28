#2742
# n = int(input())
# for i in range(n,0,-1):
#     print(i)

n = int(input())
arr=[]
for i in range(1,n+1):
    arr.append(" "*(n-i)+"*"*i)
arr+= arr[n-2::-1]

print(*arr, sep='\n')
