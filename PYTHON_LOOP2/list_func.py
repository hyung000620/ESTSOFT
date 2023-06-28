
# a = [1,2,3]
# b = [4,5,6]

# a += reversed(a)

# a.extend(b)

# a *=3

# a.insert(len(a),4)

# a.pop() 없으면 맨 마지막 값 또는 값 지정
# a.remove(3) 값 지정
# print(a.find(2))
# a= {"일일퀴즈성적":[10,20,30]}

# print(a['일일퀴즈성적'][2])

A,B,C = map(int, input().split())

arr = [A*B,B*C,A*C]
arr.sort(reverse=True)

# for i in zip(['a','b','c'],[1,2,3]):
#     print(i)
