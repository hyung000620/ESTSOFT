a=int(input())

cnt=0
for i in range((a+1)//3,(a+1)//2):
    cnt+=i-(a-i+1)//2+1
print(cnt)