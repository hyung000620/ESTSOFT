je = list(map(int, input().split()))
sp = list(map(int, input().split()))

j=s=0
flag1,flag2 = False,False
for i in range(9):
    j +=je[i]
    if j>s:
        flag1 = True
    s +=sp[i]
        
if j < s:
    flag2 = True

if flag1 and flag2:
    print("Yes")
else:
    print("No")