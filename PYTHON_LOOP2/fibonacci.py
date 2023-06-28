'''
피보나치 수열
a[n] = a[n-2]+a[n-1]
'''

n = int(input())
curr,next = 0,1
for i in range(n):
    curr, next = next, next+curr
print(curr)