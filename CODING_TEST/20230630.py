# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())

# b = [i for i in range(1,n+1)]

# for i in range(m):
#     i,j,k = map(int, input().split())
#     b = b[:i-1]+b[k-1:j]+b[i-1:k-1]+b[j:]

# print(*b,sep=' ')

# t = int(input())
# for i in range(t):
#     n = int(input())
#     print(int(n ** 0.5))

# a = [0]*26
# b = a[:]
# ans = 0

# for i in input():
#     a[ord(i)-97] += 1
# for i in input():
#     b[ord(i)-97] += 1
# for i in range(26):
#     ans += abs(a[i]-b[i])
# print(ans)

# card = [i for i in range(21)]

# for i in range(10):
#     i,j = map(int,input().split())
#     card = card[:i]+list(reversed(card[i:j+1]))+card[j+1:]    
#     # card = card[i:j+1]=card[j:i-1:-1]

# print(*card[1:],sep=' ')

# import sys
# input = sys.stdin.readline

# a,b = map(int, input().split())
# n1,n2 = min(a,b),max(a,b)
# arr = [i for i in range(n1+1,n2)]
# n = n2-n1-1
# if n1 == n2 or n1+1 == n2:
#     n = 0
# print(n)
# print(*arr, sep=' ')

# h1,m1,s1 = map(int, input().split(":"))
# h2,m2,s2 = map(int, input().split(":"))

# time = (h2*3600+m2*60+s2)-(h1*3600+m1*60+s1)
# if time<0:time+=3600*24
# t1,t2,t3= time//3600,(time%3600)//60,time%60

# print("%02d:%02d:%02d" %(t1,t2,t3))

# N = [int(i) for i in input()]

# a = sum(N[:len(N)//2])
# b = sum(N[len(N)//2:])

# if a==b:print("LUCKY")
# else:print("READY")

# arr = list(map(int, input().split()))

# di = dict()
# for i in arr:
#     x,y = map(int,input().split())
#     di.update({x:y})

# di = dict(sorted(di.items(), reverse=True))

# result = 0
# for idx, (k,v) in enumerate(di.items()):
#     result += (v-k)*arr[idx]
# print(result)

# arr = [0]*100
# a1,a2,a3 = map(int, input().split())

# for i in range(3):
#     x,y = map(int, input().split())
#     for j in range(x,y):
#         arr[j]+=1

# print(arr.count(3)*a3*3+arr.count(2)*a2*2+arr.count(1)*a1)

# import sys
# input = sys.stdin.readline

# N = int(input())
# min_num = 1001

# for i in range(N):
#     A,B = map(int, input().split())
#     if A<=B:min_num = min(B,min_num)

# print(-1 if min_num==1001 else min_num)

# person = list(map(int, input().split()))
# x,y,r = map(int, input().split())

# try:
#    print(person.index(x)+1) 
# except:
#     print(0)

# T = int(input())
# for i in range(T):
#     a,b,c = map(int,input().split())
#     print(min(a,b,c))

# import sys
# input = sys.stdin.readline
# N = int(input())
# chicken = list(map(int, input().split()))
# result = 0
# for i in chicken:
#     result += min(N,i)
# print(result)

# import sys
# input = sys.stdin.readline

# N = int(input())
# arr = ["Gnomes:"]
# for i in range(N):
#     st = "Unordered"
#     a,b,c = map(int,input().split())
#     if a<=b<=c or a>=b>=c: st="Ordered"
#     arr.append(st)

# print(*arr,sep='\n')

def find_minimum_video_size(N, M, lecture_lengths):
    # 가능한 영상 크기의 최소값과 최대값 초기화
    start = max(lecture_lengths)
    end = sum(lecture_lengths)
    
    result = 0

    # 이분 탐색을 통해 가능한 영상 크기의 최소값을 구함
    while start <= end:
        mid = (start + end) // 2  # 가능한 영상 크기의 중간값
        
        count = 1  
        total_length = 0  # 현재 영상 파일의 길이 초기화
        
        for length in lecture_lengths:
            if total_length + length > mid:
                count += 1
                total_length = 0
            
            total_length += length  
        
        if count <= M:
            result = mid
            end = mid - 1
        else:
            start = mid + 1
    
    return result


# 입력 예시
N, M = map(int, input().split())
lecture_lengths = list(map(int, input().split()))

# 함수 호출 및 결과 출력
result = find_minimum_video_size(N, M, lecture_lengths)
print(result)