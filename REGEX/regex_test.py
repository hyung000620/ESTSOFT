#Regular Experession

import re

# pattern = r'apple'
# string = "I have an apple and an orange"

# result = re.search(pattern,string)
# print(result)

# pattren = r"a[bcd]*d"

# string = "ab, abcd, abbcd, acd"

# result = re.findall(pattren,string)

# print(result)

# pattern = r"b.t"
# string = "bat, bet, bit, but, aut"

# pattern = r"ab*c"
# string = "ac, abc, abbc, abdbc"

# pattern = r"(ab)+c"
# string = "ac, abc, abbc, abdbc, ab, aabbc"

# pattern = r"\d+"
# string = "I have 10 apples and 5 bananas"


# pattern = r"\w+"
# string = "I have 10 apples and 5 bananas!"

# pattern = r"^Hello"
# string = "Hello, World! Hello, python"
# result = re.findall(pattern, string)
# print(result)

pat = r"전화번호는 [0-9-]+{10,11}"
st= "나의 전화번호는 !-010-1234-5678입니다. 다른 전화번호는 !-02-9876-5432-!가 있습니다."

pat = r"\w+@[a-z.]+"
st = "안녕하세요. 이메일 주소는 abc@example.com입니다. 다른 이메일은 ab_TE@hcu.co.kr이고, x_yz@hotmail.net도 있습니다."

pat = r"[a-z:/]+\.[a-z./,]+"
st = "문장 속에는 다양한 URL이 있습니다. https://www.example.com/, http://subdomain.example.co.kr/, www.google.com, ftp://fileserver.example.org, 이렇게 다양한 형식의 URL이 있습니다."
res = re.findall(pat,st)
res = re.sub(pat, "",st)
print(res)
