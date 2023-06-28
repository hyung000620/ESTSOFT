
# N = int(input())

# for i in range(N):
#     print(" "*i+"*"*(N-i))

#한번 쓰는 방법
# for i in range(1,N+1):
#     print("*"*i)

#두번 쓰는 방법

# N = int(input())

# for i in range(1,N+1):
#     print(" "*(N-i)+"*"*i)


# for i in range(N):
#     print("*"*N)

a = [i for i in range(1,6)]
a += [i for i in range(7, 10)]

print(a)

