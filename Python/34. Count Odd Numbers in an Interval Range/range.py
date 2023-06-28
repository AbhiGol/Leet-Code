low = 8
high = 10
count = 0

for i in range(low,high+1):
    if i % 2 != 0:
        count += 1

print(count)