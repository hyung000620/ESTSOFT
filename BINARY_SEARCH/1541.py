# plus = input().split("+")

# li = []
# for i in plus:
#     if "-" in i:
#         minus= list(map(lambda x: str(int(x)),i.split("-")))
        
#         li.append("-".join(minus)) 
#     else:
#         li.append(str(int(i)))

# st = "+".join(li)

# s1 = sum(map(eval, st.split("+")))
# s2 = list(map(lambda x: str(eval(x)), st.split("-")))
# s2 = eval("-".join(s2))

# print(min(s1,s2))

# l=int(input())

# sum=0

# for i in l[0].split('-'):
#     sum+=int(i)
# for i in l[1:]:
#     for j in i.split('+'):
#         sum-=int(j)
# print(sum)