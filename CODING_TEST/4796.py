
idx = 1
while True:
    L,P,V = map(int, input().split())
    
    res = 0
    if L==P==V==0:break
    
    res += L*(V//P)
    res += min(V%P,L)
    
    print(f"Case {idx}: {res}")
    idx+=1