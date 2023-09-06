from sys import stdin
input = stdin.readline

W,H,X,Y,P = map(int, input().split())
cnt = [0]

def radius(x,y):
    return ((x)**2 + (y)**2)**0.5

def main():
    for _ in range(P):
        x,y = map(int, input().split())

        if (X<= x <= X+W) and (Y <= y <= Y+H):
            cnt[0] += 1
            continue

        R = H//2
        left = radius((x-X),(y-(Y+R)))
        right = radius((x-(X+W)),(y-(Y+R)))
        if left <=R or right <= R:
            cnt[0] += 1

if __name__ == "__main__":
    main()
    print(cnt[0])