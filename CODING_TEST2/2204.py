from sys import stdin
input = stdin.readline

res = []
while True:
    n = int(input())
    if n == 0: break;
    
    alphabet = dict()
    for _ in range(n):
        word = input().rstrip()
        alphabet[word.lower()] = word
    
    alphabet = sorted(alphabet.items(),key=lambda x: x[0])
    res.append(alphabet[0][1])  

print(*res,sep='\n')