nums = [-1,1,-1,1,-1]
product = 1

for i in range(0,len(nums)):
    product *= nums[i]

if product < 0:
    print("-1")
elif product == 0:
    print("0")
else:
    print("1")