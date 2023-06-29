nums = [1,3,4,2,2]
slow = nums[0]
fast = nums[0]

while True:
    slow = nums[slow]
    fast = nums[nums[fast]]
    if slow == fast:
   		break

num1= nums[0]
num2 = slow
while num1 != num2:
    num1 = nums[num1]
    num2 = nums[num2]
print(num2)