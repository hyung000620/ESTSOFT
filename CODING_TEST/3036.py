import sys
input = sys.stdin.readline

def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
n = int(input())
li = list(map(int, input().split()))
for i in range(1, n):
    g = gcd(li[0], li[i])
    print('{0}/{1}'.format(li[0]//g, li[i]//g))