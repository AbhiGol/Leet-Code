nums = [4,3,2,7,8,2,3,1]

result = []
for num in nums:
    index = abs(num)-1
    if nums[index] > 0:
        nums[index]*=-1
for index, num in enumerate(nums):
    if num >0:
        result.append(index+1)
print(result)