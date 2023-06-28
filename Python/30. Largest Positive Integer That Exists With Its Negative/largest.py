nums = [-10,8,6,7,-2,-3]
largest = 0

for i in range(1,len(nums)):
    if abs(nums[i-1]) == abs(nums[i]):
        largest < nums[i]
        largest = nums[i]

if largest == 0:
    print(-1)
else:
    print(abs(largest))