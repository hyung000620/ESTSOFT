n=int(input())
s=list(input())

dna = {"AA" : "A", "AG" : "C", "AC" : "A", "AT" : "G", "GA" : "C","GG" : "G",
       "GC" : "T", "GT" : "A", "CA" : "A", "CG" : "T", "CC" : "C", "CT" : "G",
       "TA" : "G", "TG" : "A", "TC" : "G","TT" : "T"}

for i in range(n - 2, -1, -1):
    s[i] = dna[s[i] + s[i + 1]]
    s[i + 1] = ""
print(s[0])