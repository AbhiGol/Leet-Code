nums = [1,3,5,4,7]

if not nums:
    print("0")
start, result = 0, 1
for end in range(1, len(nums)):
    if nums[end-1] >= nums[end]:
        start = end
    result = max(result, end-start+1)
print(result)