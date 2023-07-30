import sys
input = sys.stdin.readline


def palindrome():
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i==j:
                continue
            word = arr[i]+arr[j]
            if word == word[::-1]:
                return word
    return 0

t = int(input())
for _ in range(t):
    k = int(input())
    arr = [input().rstrip() for _ in range(k)]
    ans = palindrome()
    print(ans if ans else 0)
                

        
    
    
    