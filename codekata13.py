nums = [0,1,0,3,12]
def move_zeroes(nums):
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if nums[i] == 0:
                nums[i] , nums[j] = nums[j], nums[i]

    return nums                 


a = move_zeroes(nums)
print(a)