N = int(input())
ans = []

for i in range(1, N+1):
    first = N
    second = i
    tmp = [N, i]
    
    while True:
        next_num = first - second
        if next_num >= 0:
            tmp.append(next_num)
            first ,second = second,next_num
        else:
            if len(tmp) > len(ans):
                ans = tmp
            break
print(len(ans))
print(*ans)