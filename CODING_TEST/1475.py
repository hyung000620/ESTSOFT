N = input()
nums = {i:0 for i in range(10)}

for i in range(len(N)):
    tmp = int(N[i])
    if tmp == 9 or tmp == 6:
        if nums[9]<nums[6]:
            nums[9]+=1
        else:
            nums[6]+=1
    else:
        nums[tmp]+=1
        
max_num = max(nums.values())
print(max_num)
    
    