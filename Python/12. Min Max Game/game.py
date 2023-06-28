nums = [1,3,5,2,4,8,2,2]

len = len(nums)/2

while len != 0:
    for i in range(0,int(len)):
        if i%2 == 0:
            nums[i] = min(nums[2*i], nums[2*i+1])
        else:
            nums[i] = max(nums[2*i], nums[2*i+1])
    len = len/2
print(nums[0])