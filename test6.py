N = int(input())
arr = list(map(int, input().split()))
arr.sort()
left, right = 0, N * arr[-1]

while left < right:
    mid = (left + right) // 2
    total = sum(mid // time for time in arr) 

    if total >= N:
        right = mid
    else:
        left = mid + 1

print(left)
