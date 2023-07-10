import sys
input = sys.stdin.readline
N = int(input())

people = sorted(map(int,input().split()))

result,tmp = 0,0
for i in people:
    tmp+=i
    result +=tmp
        
print(result) 