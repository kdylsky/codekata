nums = [-2,1,-3,4,-1,2,1,-5,4]

def maxSubArray(nums):
    max = 0
    start_idx = 0
    end_idx = 0
    for i in range(len(nums)):
        sum = 0
        
        for j in range(i, len(nums)):
            sum += nums[j]
            
            if max < sum:     
                max = sum
                start_idx = i
                end_idx = j

    return f"max: {max} start_idx: {start_idx} end_idx: {end_idx}"
    
result = maxSubArray(nums)

print(result)