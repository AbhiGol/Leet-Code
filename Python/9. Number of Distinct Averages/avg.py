nums = [4,1,4,0,3,5]
nums.sort()

print(nums)
len1 = len(nums)
for i in range(0,len(nums)//2):
    sum = (nums[i] + nums[len1-1])/2
    len1 = len1 - 1
print(sum)