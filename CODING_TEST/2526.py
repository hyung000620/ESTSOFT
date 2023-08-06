N, P = map(int, input().split())

tmp = N
li = []
while True:
    tmp = tmp*N%P
    if tmp in li:
        break
    else: 
        li.append(tmp)

print(len(li)-li.index(tmp))
    