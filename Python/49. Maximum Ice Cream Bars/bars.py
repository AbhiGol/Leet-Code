costs = [1,6,3,1,2,5]
coins = 20
sum = 0
count = 0
costs.sort()

for i in range(0,len(costs)):
    sum += costs[i]
    if sum <= coins:
        count += 1

print(count)