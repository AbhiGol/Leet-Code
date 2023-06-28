nums = [10,23,45,67,89]

separated_digits = []
for num in nums:
    num_str = str(num)
    for digit_str in num_str:
        digit = int(digit_str)
        separated_digits.append(digit)
print(separated_digits)