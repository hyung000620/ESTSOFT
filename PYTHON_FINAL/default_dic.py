# from collections import defaultdict

# my_dic = defaultdict(int)

# my_dic['사과']+=1
# my_dic['바나나']+=1
# my_dic['수박']+=1


# print(my_dic)

# 정답 <10, 1, 3, 6, 2, 9, 5, 7, 4, 8>

# n,k = map(int,input().split())
# arr = [i for i in range(1,n+1)]
# queue = []
# while len(arr)!=0:
#     for i in range(k-1):
#         arr.append(arr.pop(0))
#     queue.append(arr.pop(0))
    
# st = ', '.join(map(str,queue))
# print(f"<{st}>")