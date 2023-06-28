candies = [4,2,1,1,2]
extraCandies = 1
result = []
most_candies = max(candies)

for i in range(0,len(candies)):
    if candies[i] + extraCandies >= most_candies:
        result.append(True)
    else:
        result.append(False)
print(result)