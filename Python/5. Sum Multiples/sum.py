n = 9
sum = 0

for i in range(2,n+1):
    if i%3 == 0 or i%5 == 0 or i%7 == 0:
        sum = sum + i

print(sum)