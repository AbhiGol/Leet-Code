import math

n = 26

if n <= 0:
    print(False)

print(math.log10(n)/math.log10(3)%1 == 0)