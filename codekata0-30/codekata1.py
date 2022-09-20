nums = [331,53,2,21,3,24,]

def selectionSort(nums):
    count = 0
    for i in range(len(nums)):
        
        min_num = min(nums[i:len(nums)])
        if min_num < nums[i]:
            # nums[i],nums[nums.index(min_num)] = nums[nums.index(min_num)],nums[i]
            nums[nums.index(min_num)],nums[i] = nums[i], nums[nums.index(min_num)]
            count += 1
            print(nums)
    print("-------------------------")
    return nums, count
    
result = selectionSort(nums)
print(result)

# nums[nums.index(3)], nums[nums.index(5)] = nums[nums.index(5)], nums[nums.index(3)]
# print(nums.index(3))
# print(nums.index(5))

# print(nums)
