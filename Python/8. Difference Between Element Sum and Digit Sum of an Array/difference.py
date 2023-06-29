nums = [23, 456, 71]
digit_sum = 0
number_sum = 0
for num in nums:
    number_sum += num
    num_str = str(num)
    for digit_str in num_str:
        digit = int(digit_str)
        digit_sum += digit
print(abs(digit_sum - number_sum))