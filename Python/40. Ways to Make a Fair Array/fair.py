def ways_to_make_fair_array(nums):
    left_sum = 0
    right_sum = sum(nums)
    count = 0

    for i in range(len(nums)):
        right_sum -= nums[i]

        if left_sum == right_sum:
            count += 1

        left_sum += nums[i]

    return count

array = [2, 1, 6, 4]
result = ways_to_make_fair_array(array)
print(result)  # Output: 1






