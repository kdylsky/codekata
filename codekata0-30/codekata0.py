nums = [-1,0,3,5,9,12,15,16,18,20,39,40]
target = 0

def serch(nums, target):
    idx = 0
    for i in nums:
        if i == target:
           return idx
        else:
            idx = idx +1
    
        if idx == len(nums):
            return -1    
result = serch(nums, target) 

def search(nums, target):
    min_idx = 0
    max_idx = len(nums)-1
    count = 0
    
    while nums[int((min_idx+max_idx)/2)] != target:    
        if nums[int((min_idx+max_idx)/2)] < target:
            min_idx = int((min_idx+max_idx)/2) +1
            
        else:
            max_idx = int((min_idx+max_idx)/2) -1
        
        count = count+1
        
        if count > len(nums)/2:
            return -1
        
    return int((min_idx+max_idx)/2)


result = search(nums, target)
print(result)