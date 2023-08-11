max_num = 0; num = 0
for i in range(1, 6):
    a = list(map(int, input().split()))
    if max_num < sum(a):
        max_num = sum(a)
        num = i

print(num, max_num)