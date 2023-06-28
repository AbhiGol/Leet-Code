nums = [0,1]
num = []
for i in range(1,len(nums)):
    if nums[i-1] == nums[i]:
       nums[i-1] = nums[i-1] *2
       nums[i] = 0
    else:
        nums[i-1] = nums[i-1]
        
count = 0
for i in range(0,len(nums)):
    if nums[i] == 0:
        count += 1
    else:
        num.append(nums[i])

for i in range(0,count):
    num.append(0)
print(num)     