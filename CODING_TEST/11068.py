t = int(input())

for i in range(t):
    n = int(input())
    ans = []
    for j in range(2,65):
        li = []
        tmp = n
        while tmp!=0:
            li.append(tmp%j)
            tmp=tmp//j
        for k in range(len(li)//2):
            if(li[k]!=li[-1-k]):
                ans.append('X')
                break
            
    if len(ans)==63:
        print(0)
    else:
        print(1)
    
        