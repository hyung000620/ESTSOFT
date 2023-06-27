# N, M = map(int, input().split())

# max_num = 0
# number = N+1
# if N<M: number=M+1
# for i in range(1,number):
#     if N%i ==0 & M%i==0: max_num=i
    
# print(max_num)

# a, b = map(int,input().split())

#최대공약수
# def GCD(a,b):
#     while b!=0:
#         a,b = b, a%b
#     return a
'''
최소공배수를 구하기 위해서는 두 수의 곱에서 최대공약수를  나누면 된다.
'''
    
# print(f"최댁공약수 : {GCD(a,b)}, 최소공배수{a*b/GCD(a,b)}")

# 소인수 분해
n = int(input("소인수 분해할 숫자를 입력해주세요."))
factors = []


while n%2 == 0:
    factors.append(2)
    n //=2
    
i = 3

while i*i <=n:
    while n % i ==0:
        factors.append(i)
        n //=i
    i +=2

if n >1:
    factors.append(n)
print(factors)
