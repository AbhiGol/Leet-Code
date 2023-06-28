def max_ascending_subarray_sum(nums):
    max_sum = 0  
    curr_sum = 0 
    for i in range(len(nums)):
        if i == 0 or nums[i] > nums[i-1]:
            curr_sum += nums[i]
        else:
            curr_sum = nums[i]

        max_sum = max(max_sum, curr_sum)

    return max_sum

nums = [12,17,15,13,10,11,12]
print(max_ascending_subarray_sum(nums))  
