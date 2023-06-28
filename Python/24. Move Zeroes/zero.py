nums = [0,1,0,3,2,0,0,12]
num = []
nums.sort()
count = 0

for i in range(0,len(nums)):
    if nums[i] == 0:
        count += 1
    else:
        num.append(nums[i])

for i in range(0,count):
    num.append(0)
  
print(num)