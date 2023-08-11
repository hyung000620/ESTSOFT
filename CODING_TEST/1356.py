N = input()

def prod(iter):
    res = 1
    for val in iter:
        res *= val
    return res

flag = any(
    prod(map(int, N[:i])) == prod(map(int, N[i:]))
    for i in range(1, len(N))
)

print("YES" if flag else "NO")