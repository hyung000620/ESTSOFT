import sys
input = sys.stdin.readline

n = int(input())

books = dict()
for i in range(n):
    book = input().rstrip()
    
    if book in books:
        books[book] +=1
    else:
        books[book] = 1

val = max(books.values())
books = sorted(books.items(), key = lambda x:x[0])

for k,v in books:
    if v==val:
        print(k)
        break