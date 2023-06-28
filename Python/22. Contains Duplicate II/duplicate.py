nums = [1,2,3,1,2,3]
k = 2
count = 0

for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        #if nums[i] == nums[j] and abs(i-j) <= k:
        #   count += 1
        if nums[i] == nums[j] and abs(i-j) > k:
            count += 1

if count > 0:
    print("False")
else:
    print("True")