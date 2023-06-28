nums = [1,2,4,7,10]
sum = 0

for i in range(0,len(nums)):
    if nums[i] % 2 == 0:
        if nums[i] % 3 == 0:
            sum += nums[i]
    
print(sum/2)