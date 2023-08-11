a=int(input())
for i in range(a):
    b=input()
    t=int(len(b)**(1/2))
    r=''
    for s in range(t):
        r+=b[t-1-s:len(b):t]
        print(r)
    print(r)
    