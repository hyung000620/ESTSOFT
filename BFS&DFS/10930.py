import hashlib

s = input()
res = hashlib.sha256(s.encode())
print(res.hexdigest())