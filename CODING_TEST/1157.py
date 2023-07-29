# word=input().upper()
# lst=[]
# for i in range(65,91):
#     cnt=word.count(chr(i))
#     lst.append(cnt)
# sorted=sorted(lst,reverse=True)
# if sorted[0]==sorted[1]:
#     print("?")
# else:
#     print(chr(lst.index(sorted[0])+65))

count = dict()
if 1 in count:
    count[1] += 1
else:
    count = 1
a = [1,2,3]

print(count)