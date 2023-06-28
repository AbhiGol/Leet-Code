n = 17
lnum = [n]
while n != 1:
    if n % 2 == 0:
        n = n//2
        lnum.append(n)
    else:
        n = (3*n) + 1
        lnum.append(n)
print("Hailstone : ",lnum)