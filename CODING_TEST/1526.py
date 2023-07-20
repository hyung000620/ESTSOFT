N = int(input())

while True:
    res = True
    for i in str(N):
        if i!='4'and i!='7':
            res= False
            N-=1
    if res:
        print(N)
        break