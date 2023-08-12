"""
실버2 사탕게임
같은 행에 있는 인접한 사탕끼리 바꿔주고 체크하고, 체크를 했으면 다시 바꿔주고
동일하게 같은 열에 있는 인접한 사탕끼리 바꿔주고 체크하고, 체크를 했으면 다시 바꿔주는 방식으로
문제를 해결하였습니다.
"""
import sys
input = sys.stdin.readline

def check(candy):
    max_cnt = 1
    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if candy[i][j] == candy[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)

        cnt = 1
        for j in range(1, N):
            if candy[j][i] == candy[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)
    
    return max_cnt

N = int(input())
candy = [list(input().rstrip()) for _ in range(N)]
ans = 0

for i in range(N):
    for j in range(N):
        if j + 1 < N:
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
            cnt = check(candy)
            ans = max(ans, cnt)
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]

        if i + 1 < N:
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
            cnt = check(candy)
            ans = max(ans, cnt)
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]

print(ans)