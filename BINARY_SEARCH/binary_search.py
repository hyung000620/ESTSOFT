import time

def time_calc(func):
    def calc(*args, **kwargs):
        stime = time.time()
        result = func(*args,**kwargs)
        etime = time.time()
        return f"{result} {etime-stime:.7f}"
    return calc

# @time_calc
# def binary_search(start, end, target, arr):
#     mid = (start+end)//2
#     if arr[mid]==target:
#         return mid
#     elif arr[mid] > target:
#         return binary_search(start, mid+1, target, arr)
#     else:
#         return binary_search(mid-1, end, target, arr)



# li = [1,4,9,16,25,31]
# print(binary_search(0,len(li)-1,4,li))

# # 이진탐색
# def binary_search(find, arr):
    
#     start = 0
#     end = len(arr)-1
    
#     while start<=end:
#         mid = (start+end)//2
        
#         if arr[mid] == find:
#             return 1
#         elif  arr[mid] < find:
#             start = mid+1
#         else:
#             end = mid -1
#     return 0
            
# n = int(input())
# li = sorted(map(int,input().split()))
# m = int(input())
# li2 = list(map(int, input().split()))

# for i in li2:
#     print(binary_search(i,li))


