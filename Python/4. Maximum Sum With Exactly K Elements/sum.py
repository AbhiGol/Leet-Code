nums = [4, 2, 9, 7, 6]
k = 3

nums.sort()
last = nums[len(nums)-1]
first = last
count = 1

for i in range(k-1):
    last = last + 1
    first = first + last
    
print(first)
