N = int(input())

li = [input() for _ in range(N)]

li.sort()

print(*li, sep='\n')