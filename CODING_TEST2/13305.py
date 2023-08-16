from sys import stdin
input = stdin.readline

def solve(distance, city, N):
    res = distance[0]*city[0]
    price = city[0]
    
    for i in range(1,N-1):
        if price > city[i]:
            price = city[i]
        res += price* distance[i]
            
    return res

def main():
    N = int(input())
    distance = list(map(int, input().split()))
    city = list(map(int, input().split()))

    print(solve(distance,city,N))
    
if __name__ == "__main__":
    main()