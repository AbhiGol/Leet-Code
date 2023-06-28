nums = [4,6,0,5,8,10,12,1]
num = []
nums.sort()
j = 0
for i in range(nums[0],nums[len(nums)-1]):
    if i == nums[j]:
        j += 1
    else:
        num.append(i)
print(num) 