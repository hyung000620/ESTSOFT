import sys
input = sys.stdin.readline

N = int(input())

card = dict()
for _ in range(N):
    c = int(input())
    
    if c in card:
        card[c]+=1
    else:
        card[c]=1

res = sorted(card.items(), key=lambda x: (-x[1],x[0]))
print(res[0][0])