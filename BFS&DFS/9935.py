import sys
input= sys.stdin.readline

s = input().rstrip()
bom = input().rstrip()

stack = []
len_bom = len(bom)
for i in range(len(s)):
    stack.append(s[i])
    if ''.join(stack[-len_bom:])==bom:
        for j in range(len_bom):
            stack.pop()
 
if stack:
    print(''.join(stack))
else:
    print('FRULA')