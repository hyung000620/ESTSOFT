import sys
input = sys.stdin.readline

K,N = map(int, input().split())

numbers=[]
max_len = max_num = 0
for i in range(K):
    tmp = input().strip()
    numbers.append(tmp)
    max_num= max(max_num,int(tmp))

for i in range(N-K):
    numbers.append(str(max_num))
numbers.sort(key=lambda x: x*10,reverse=True)
print("".join(numbers))