"""
LIS(Longest Increasing Subsequence) 알고리즘을 사용하여 책들을 배열하는 최소 횟수를 계산하였습니다.
책들의 배열 순서를 탐색하면서 LIS(최장 증가 부분 수열)를 구성하고, 교체해야 할 위치를 찾아 교체 횟수를 늘립니다.
"""
def lower_bound(start, end, target, LIS):
    while start < end:
        mid = (start + end) // 2
        if LIS[mid] < target:
            start = mid + 1
        else:
            end = mid
    return end

def main():
    N = int(input())
    books = list(map(int, input().split()))
    
    ans = 0
    LIS = [0] * N
    LIS[0] = books[0]
    j = 0
    
    for i in range(1, N):
        if LIS[j] < books[i]:
            j += 1
            LIS[j] = books[i]
        else:
            pos = lower_bound(0, j, books[i], LIS)
            LIS[pos] = books[i]
            ans += 1
    
    print(ans)

if __name__ == "__main__":
    main()