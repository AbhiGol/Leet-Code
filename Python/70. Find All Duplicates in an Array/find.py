nums = [4,3,2,7,8,2,3,1]

result = []
for _, num in enumerate(nums):
    index = abs(num)-1
    if nums[index] < 0:
        result.append(index+1)
    nums[index]*=-1
print(result)