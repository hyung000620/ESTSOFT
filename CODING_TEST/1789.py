s = int(input())

tmp = 0
res = 0
while True:
    tmp +=1
    res +=tmp
    if res>s:
        break

print(tmp-1)