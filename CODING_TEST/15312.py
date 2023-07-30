alpha = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

A = input()
B = input()
arr = []

for i in range(len(A)):
    arr.append(alpha[ord(A[i])-65])
    arr.append(alpha[ord(B[i])-65])

dp = []
while len(arr)!=2:
    for i in range(1,len(arr)):
        dp.append((arr[i]+arr[i-1])%10)
    arr = dp
    dp = []

print(*arr,sep='')