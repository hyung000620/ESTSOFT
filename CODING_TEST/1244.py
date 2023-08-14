import sys
input = sys.stdin.readline

def change(num):
    if switch[num]==0:
        switch[num]=1
    else:
        switch[num]=0
    return
    
N = int(input())
switch = [-1]+list(map(int, input().split()))

student = int(input())
for _ in range(student):
    gender, num = map(int, input().split())
    
    if gender == 1:
        for i in range(num,N+1,num):

            change(i)
    else:
        change(num)
        for k in range(N//2):
            if num+k>N or num-k<1:break
            if switch[num+k] == switch[num-k]:
                change(num+k)
                change(num-k)
            else:
                break

for i in range(1,N+1):
    print(switch[i], end=" ")
    if i%20 == 0:
        print()