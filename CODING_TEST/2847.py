N = int(input())

score = [int(input()) for _ in range(N)]

cnt = 0
for i in range(N-1,0,-1):
    if score[i]<=score[i-1]:
        cnt += score[i-1]-score[i]+1
        score[i-1]= score[i]-1

print(cnt)