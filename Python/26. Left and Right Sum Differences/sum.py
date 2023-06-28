nums = [1]
leftsum = [len(nums)]
rightsum = []
totalsum = []

leftsum[0] = 0
for i in range(1,len(nums)):
    leftsum.append(leftsum[i-1]+nums[i-1])

sum = 0
for i in range (1,len(nums)):
    sum = nums[i]
    for j in range(i+1,len(nums)):
        sum += nums[j]
    rightsum.append(sum)
    sum = 0
rightsum.append(0)

for i in range(0,len(nums)):
    totalsum.append(abs(leftsum[i] - rightsum[i]))
print(totalsum)