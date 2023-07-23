n = int(input())

for i in range(n):
    a,b = input().split()
    ans = f"{a} & {b} are "
    
    a = "".join(sorted(a))
    b = "".join(sorted(b))
    
    if a == b:
        ans +="anagrams."
    else:
        ans +="NOT anagrams."
    print(ans)