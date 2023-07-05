# while True:
#     li = input().split()
#     if li[0]=="#":break
    
#     st = ''.join(li[1:]).lower()
#     print(li[0],st.count(li[0]))

# Adrian = "ABC"
# Bruno = "BABC"
# Goran = "CCAABB"

# arr = ["Adrian","Bruno","Goran"]
# li = [0,0,0]
# n = int(input())
# st = input()

# for i in range(n):
#     if st[i]==Adrian[i%3]:
#         li[0]+=1
#     if st[i]==Bruno[i%4]:
#         li[1]+=1
#     if st[i]==Goran[i%6]:
#         li[2]+=1
        
# print(max(li))

# for i in range(3):
#     if max(li)==li[i]:
#         print(arr[i])

a = input()
b = input()

print(a&b)