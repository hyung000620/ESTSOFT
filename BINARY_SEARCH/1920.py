def binary_search(find, arr):
    
    start = 0
    end = len(arr)-1
    
    while start<=end:
        mid = (start+end)//2
        
        if arr[mid] == find:
            return 1
        elif  arr[mid] < find:
            start = mid+1
        else:
            end = mid -1
    return 0
if __name__ == "__main__":
    n = int(input())
    li = sorted(map(int,input().split()))
    m = int(input())
    li2 = list(map(int, input().split()))

    for i in li2:
        print(binary_search(i,li))
