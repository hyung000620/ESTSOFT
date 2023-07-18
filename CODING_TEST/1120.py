A,B = input().split()

def dif(a,b):
    cnt = len(a)
    for i in range(len(a)):
        if a[i]==b[i]:
            cnt-=1
    return cnt

if len(A)==len(B):
    print(dif(A,B));
elif len(A)>len(B):
    tmp = len(A)-len(B)
    tmp = min(dif(A,(B+A[-tmp:])),dif(A,(A[:tmp]+B)))
    print(tmp)
else:
    tmp = len(B)-len(A)
    tmp = min(dif(B,(A+B[-tmp:])),dif(B,(B[:tmp]+A)))
    print(tmp)