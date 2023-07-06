# import re

# while True:
#     s = input()
    
#     if s=='end':break
    
#     case1 = len(re.findall('[aeiou]',s)) != 0
#     case2 = len(re.findall('[aeiou]{3}|[^aeiou]{3}',s))==0
#     case3 = len(re.findall('([a-df-np-z])\\1',s))==0
#     if case1 and case2 and case3:
#         print(f"<{s}> is acceptable.")
#     else:
#         print(f"<{s}> is not acceptable.")

# while True :
#     a = input()
#     stack = []

#     if a == "." :
#         break

#     for i in a :
#         if i == '[' or i == '(' :
#             stack.append(i)
#         elif i == ']' :
#             if len(stack) != 0 and stack[-1] == '[' :stack.pop()
#             else : stack.append(']');break
#         elif i == ')' :
#             if len(stack) != 0 and stack[-1] == '(' :stack.pop()
#             else :stack.append(')');break
            
#     print("no" if len(stack) else "yes")     
    
# import re

# text = "I love Programming. Today, I learn Crawling."

# pattern = r"\b\w+ing\b"
# result = re.findall(pattern, text)
# print(result)


# n = int(input())

# for i in range(n):
#     s = input()
#     print(int(s,2))

