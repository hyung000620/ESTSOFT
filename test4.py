# def palindrome_check1(text:str):
#     if text[::1] == text[::-1]:
#         return True
#     else:
#         return False

# def palindrome_check2(text:str):
#     for i in range(len(text)//2+1):
#         if text[i] != text[-i-1]:
#             return False
#     return True

def palindrome_check3(text:str):
    if len(text) <=2:
        return True
    if text[0] == text[-1]:
        return palindrome_check3(text[1:-1])
    else:
        return False
# def palindrome_check2(text:str):
#     for i in range(len(text)//2):
#         if text[i] != text[-i-1]:
#             return False
#     return True

print(palindrome_check3("ab"))