from collections import defaultdict

def sum_of_unique_elements(nums):
    count = defaultdict(int)

    for num in nums:
        count[num] += 1

    sum_unique = 0

    for key, value in count.items():
        if value == 1:
            sum_unique += key

    return sum_unique

array = [1, 2, 2, 3, 4, 4, 5]
result = sum_of_unique_elements(array)
print(result) 
