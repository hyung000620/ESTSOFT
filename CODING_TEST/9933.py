N = int(input())

li = [input() for _ in range(N)]

li2 = [i[::-1] for i in li]

for pw in li:
    for pw2 in li2:
        if pw == pw2:
            print(len(pw), pw[len(pw)//2])
            exit()