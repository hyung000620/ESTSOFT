# word = input()

# hap = 0
# for w in word:
#     if w.islower():
#         hap += ord(w) - 96
#     else:
#         hap += ord(w) - 38 

# isPrime = True
# for i in range(2, int(hap**0.5) + 1):
#     if hap % i == 0:
#         isPrime = False
        
# if isPrime:
#     print('It is a prime word.')
# else:
#     print('It is not a prime word.')

st = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_dict = {}
for i, char in enumerate(st):
    alphabet_dict[char] = i + 1

print(alphabet_dict)