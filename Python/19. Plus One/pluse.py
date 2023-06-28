digits = [1,3,9,9]

for i in range(len(digits)-1,0,-1):
    if digits[i] < 9:
        digits[i] += 1
        break
    digits[i] = 0
print(digits)