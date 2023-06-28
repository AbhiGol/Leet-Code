nums = [5,20,66,1314]
pos = 0
neg = 0

for i in range(0,len(nums)):
    if nums[i] < 0:
        neg += 1
    elif nums[i] > 0:
        pos += 1

if neg < pos:
    print(pos)
else:
    print(neg)