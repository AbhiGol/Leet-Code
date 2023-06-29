nums = [-1,1,0,-3,3]
new = []
pro = 1

for i in range(0,len(nums)):
    pro = pro * nums[i]

for i in range(0,len(nums)):
    new.append(int(pro/nums[i]))

print(new)