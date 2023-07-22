import sys
input = sys.stdin.readline

def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

t = int(input())

for i in range(t):
    arr = list(map(int,input().split()))
    li = []
    n = arr[0]
    arr = arr[1:]
    for i in range(n-1):
        for j in range(i+1,n):
            tmp = gcd(arr[i],arr[j])
            li.append(tmp);
    print(sum(li))