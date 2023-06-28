nums = [1,2,3,4]
count = 0

for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] == nums[j]:
            count +=1
            break
      
if count:
    print("True")
else:
    print("False")