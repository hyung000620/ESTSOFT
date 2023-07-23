# def find_checked_characters(S):
#     n = len(S)
#     char_count = {'A': 0, 'B': 0, 'C': 0}
#     unique_chars = {'A', 'B', 'C'}
#     checked_chars = 0

#     for char in S:
#         char_count[char] += 1
#         checked_chars += 1

#         if all(char_count[char] > 0 for char in unique_chars):
#             return checked_chars

# N = int(input())
# S = input().strip()

# result = find_checked_characters(S)
# print(result)



# N, D = map(int, input().split())

# sch = [input() for _ in range(N)]

# max_day = 0
# for i in range(D):
#     flag = False
#     for j in range(N):
#         if sch[j][i] == 'o':
#             flag = True
#         else:
#             flag = False
#     if flag: max_day +=1

# print(max_day)


# def max_consecutive_days(N, D, schedules):
#     max_days = 0
#     tmp = 0
#     for day in range(D):
#         consecutive_days = 0
        
#         for person in range(N):
#             if schedules[person][day] == 'o':
#                 consecutive_days += 1
        
#         if consecutive_days == N:
#             tmp +=1
#         else:
#             tmp = 0
#         max_days = max(tmp, max_days)
#     return max_days

# N, D = map(int, input().split())
# schedules = [input().strip() for _ in range(N)]

# result = max_consecutive_days(N, D, schedules)
# print(result)


# def count_reachable_ice(N, M, grid):
#     visited = [[False for _ in range(M)] for _ in range(N)]

#     def dfs(i, j):
#         if i < 0 or i >= N or j < 0 or j >= M or visited[i][j] or grid[i][j] == '#':
#             return 0

#         visited[i][j] = True
#         count = 1

#         count += dfs(i + 1, j)
#         count += dfs(i - 1, j)
#         count += dfs(i, j + 1)
#         count += dfs(i, j - 1)

#         return count

#     return dfs(1, 1)

# N, M = map(int, input().split())
# grid = [input() for _ in range(N)]

# result = count_reachable_ice(N, M, grid)
# print(result)

def max_f_value(N, M, grid):
    max_f = 0

    prefix_sum = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + grid[i - 1][j - 1]

    for lx in range(1, N + 1):
        for rx in range(lx, N + 1):
            for ly in range(1, M + 1):
                for ry in range(ly, M + 1):
                    region_sum = prefix_sum[rx][ry] - prefix_sum[rx][ly - 1] - prefix_sum[lx - 1][ry] + prefix_sum[lx - 1][ly - 1]
                    min_value = float('inf')

                    for i in range(lx, rx + 1):
                        for j in range(ly, ry + 1):
                            min_value = min(min_value, grid[i - 1][j - 1])

                    max_f = max(max_f, region_sum * min_value)

    return max_f

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

result = max_f_value(N, M, grid)
print(result)