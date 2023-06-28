n = 3 
k = 3
arr = [1,4,3]
count = 0
sum = sum(arr)


for i in range(0,n):
    if k + arr[i] > sum-arr[i]:
        count += 1
print(count)