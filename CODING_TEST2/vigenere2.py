"""
단어 중에 소문자이고 한글자만 있는경우는 원래 평문에서는 a 밖에 없는데
a 같은 경우에 key 값을 넣으면 key 값 그대로 출력을 해서 그 점을 이용해서 풀었습니다.
"""

text = """O Hsx bbg hal grmeq o diahhkjuy pwrcu ch vics ivacsu laaukrg sfqq a iwpi teokreq onsnt hji beopghrg qj a gfgi. Tus ivacsu weragh rrofc tb pwvsg kkxh wikge, nbf xhr Tqb's zcwxh jovirrr cw hr ucdeq zqrgvbipy nh vlez.

Hji bhbel hhbi jrba c litv dvaaqj, enq hji Fbl jed gc lymc tqv ig. Hji fvfux tvag le wioteq vg qifggh ig pa e lbbi aal. Gq le jonoeq chj a fvqvt qwuxaaqg enq hqsk n fwrnvbi pend cx ig, cppy gc hely gjsrg cpge zcti. Atokr aar ckavb ji tewgh, bhh kr vnwp.

Roj vg wag rqan nbf pobygh ag hji georis vb fmstiux.

"Wuov e fbcn M az," vg wavr. "Jirr W cq wrotmnt aaweyt qyt gc iit n pwrcu ch wohf ivacsu xhnh cve acv aoehj kacwpk fbf."

Crd bth le jonoeq jgvy, istc spctrfhznc."""

words = []
for i in range(1,len(text)-1):
    if text[i-1]==" " and text[i+1]==" " and text[i].islower():
        words.append((text[i],i%4))

one_words = sorted(words, key= lambda x : x[1])

key = ""
for i in one_words:
    if i[0] in key:
        continue
    key += i[0]

def vigenere_decrypt(ciphertext, keyword):
    decrypted_text = ""
    keyword = keyword.upper()

    keyword_index = 0
    for char in ciphertext:
        if char.isalpha():
            keyword_shift = ord(keyword[keyword_index % len(keyword)]) - ord(
                "A"
            )
            if char.isupper():
                decrypted_char = chr((ord(char) - ord("A") - keyword_shift) % 26 + ord("A"))
            else:
                decrypted_char = chr((ord(char) - ord("a") - keyword_shift) % 26 + ord("a"))
            keyword_index += 1
        else:
            decrypted_char = char
        decrypted_text += decrypted_char

    return decrypted_text

print(vigenere_decrypt(text,key))
print(one_words)