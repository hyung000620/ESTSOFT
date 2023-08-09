N = input()

if len(N)==1:
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
    exit()
    
flag = True
tmp = int(N[0])-int(N[1])
for i in range(len(N)-1):
    if tmp != int(N[i])-int(N[i+1]):
        flag=False
        break

if flag:
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
else:
    print("흥칫뿡!! <(￣ ﹌ ￣)>")