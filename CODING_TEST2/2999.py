S = input()
N = len(S)
R = int(N**0.5)
res = ""
while N%R:
    R-=1
for i in range(R):
    res += S[i::R]
print(res)