"""
실버3 퇴사
최대한의 상담후에 받게 되는 금액(큰 문제) 를 구하기 위해 일단 작은 문제로
나누고, 그 작은 문제들은 다른 곳에 기록해둠으로써 재사용하여 문제를 해결하였습니다.
"""
N = int(input())

sch = []
for i in range(N):
    li = list(map(int,input().split()))
    sch.append(li)

dp = [0]*(N+1)
for i in range(N):
    for j in range(i+sch[i][0],N+1):
        if dp[j]<dp[i]+sch[i][1]:
            dp[j]=dp[i]+sch[i][1]

print(dp[-1])