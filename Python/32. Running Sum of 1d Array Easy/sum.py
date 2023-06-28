nums = [3,1,2,10,1]
total_sum = []
sum = 0
for i in range(len(nums)):
    sum += nums[i]
    total_sum.append(sum)
print(total_sum)