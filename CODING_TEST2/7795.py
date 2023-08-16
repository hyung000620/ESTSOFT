from sys import stdin
input = stdin.readline

def search(A,B,m):
    cnt = 0
    i = 0
    for a in A:
        while i < m and a > B[i]:
            i += 1
        cnt += i
    return cnt
    
    return cnt

def main():
    T = int(input())
    res = []
    for _ in range(T):
        a_cnt,b_cnt = map(int, input().split())
        A = sorted(map(int, input().split()))
        B = sorted(map(int, input().split()))
        
        if max(A)<min(B):
            res.append(0)
            continue
        res.append(search(A,B,b_cnt))
        
    print(*res,sep='\n')
if __name__ == "__main__":
    main()
    