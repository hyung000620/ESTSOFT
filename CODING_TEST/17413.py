string = input()

stack = []
res = ""
flag = False

for st in string:
    if st == " ":
        while stack:
            res +=stack.pop()
        res+=st
    elif st == "<":
        while stack:
            res += stack.pop()
        flag = True
        res +=st
    elif st == ">":
        flag = False
        res+= st
    elif flag:
        res += st
    else:
        stack.append(st)
while stack:
    res+= stack.pop()
print(res)

        