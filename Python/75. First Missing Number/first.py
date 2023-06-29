num = [9,6,4,2,3,5,7,0,1]
totalSum = sum(num)
n = len(num)
expectedSum = (n*(n+1))/2
print(expectedSum - totalSum)