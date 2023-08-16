R,C,ZR,ZC = map(int,input().split())

scan = []
for _ in range(R):
    S = input()
    tmp = ""
    for i in S:
        tmp += i*ZC
    for i in range(ZR):
        scan.append(tmp)

print(*scan, sep='\n')