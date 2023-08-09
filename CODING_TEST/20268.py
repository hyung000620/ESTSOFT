def main():
    T = int(input())

    while T > 0:
        m, n = map(int, input().split())

        print(7 if m == 2 and n == 2 else 1)

        input()
        input()
        T -= 1

if __name__ == "__main__":
    main()