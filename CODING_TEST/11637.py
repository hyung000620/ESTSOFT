import sys
input = sys.stdin.readline

T = int(input())

res = []
for _ in range(T):
    n = int(input())
    li = [int(input()) for _ in range(n)]
    sum_val = sum(li)
    r_dict = dict()
    for idx,val in enumerate(li):
        r_dict[idx+1] = val
    r_dict = sorted(r_dict.items(), key=lambda x: -x[1])
    
    if r_dict[0][1] == r_dict[1][1]:
        res.append("no winner")
    elif r_dict[0][1]>sum_val//2:
        res.append(f"majority winner {r_dict[0][0]}")
    else:
        res.append(f"minority winner {r_dict[0][0]}")

print(*res,sep='\n')