nums = [4,1,3,3]
count = 0

for i in range(0,len(nums)):
    for j in range(0,len(nums)):
        if i < j:
            if (j - i) != nums[j] - nums[i]:
                count += 1
print("Number of Bad Pairs : ", count)