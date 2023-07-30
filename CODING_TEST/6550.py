import sys
input = sys.stdin.readline

while True:
    try:
        s,t = input().split()
        
        val = 0
        flag = False
        for i in range(len(t)):
            if t[i] == s[val]:
                val +=1
                if val == len(s):
                    flag = True
                    break
        print("Yes" if flag else "No")
    except:
        break
    

    