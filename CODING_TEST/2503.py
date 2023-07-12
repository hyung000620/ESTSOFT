import sys
from itertools import permutations

input = sys.stdin.readline
game = list(permutations([i for i in range(1,10)],3))
N = int(input())

for _ in range(N):
    num,strike,ball = map(int,input().split())
    
    num = list(map(int, str(num)))
    rcnt=0
    for i in range(len(game)):
        s=b=0
        i-=rcnt
        for j in range(3):
            if game[i][j] == num[j]:
                s +=1
            elif num[j] in game[i]:
                b +=1
        if strike!= s or ball!=b:
            game.remove(game[i])
            rcnt+=1

print(len(game))
        