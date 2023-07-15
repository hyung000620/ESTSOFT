st = input()
n = len(st)
li = []
for i in range(1,n-1):
    for j in range(i+1,n):
        tmp = (st[:i])[::-1]+(st[i:j])[::-1]+(st[j:])[::-1]
        li.append(tmp)

li.sort()
print(li[0])