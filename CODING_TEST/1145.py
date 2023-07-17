def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

a = sorted([*map(int, input().split())])

ret = 987654321
for i in range(5):
    for j in range(i + 1, 5):
        for k in range(j + 1, 5):
            ret = min(ret, lcm(a[i], lcm(a[j], a[k])))

print(ret)