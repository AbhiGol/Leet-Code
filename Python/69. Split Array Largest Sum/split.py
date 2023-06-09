nums = [7,2,5,10,8]
m = 2

left, right = max(nums), sum(nums)
        
while left < right:
    mid = left + ((right-left) >> 1)
    curr_sum, invalid, groups = 0, True, 0
    for num in nums:
        if num > mid:
            inalid = False
            break
        if num + curr_sum > mid:
            groups += 1
            curr_sum = 0
        curr_sum += num
    if invalid and groups < m:
        right = mid
    else:
        left = mid + 1
print(left)
 