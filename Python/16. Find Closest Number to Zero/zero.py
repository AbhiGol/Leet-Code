nums = [7,9,6,5,8]
num = []
for i in range(0,len(nums)):
    num.append(abs(nums[i]) - 0)
num.sort()
print("Closest number of zero is : ",num[0])