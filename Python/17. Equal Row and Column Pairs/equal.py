grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]

count = 0
num = 0

for i in range(0,len(grid[0])):
    for j in range(0,len(grid[0])):
        for k in range(0,len(grid[0])):
            if grid[k][i] == grid[j][k]:
                count += 1
        if count < len(grid[0]):
            count = 0
        elif count == len(grid[0]):
            num += 1
            count = 0
print("Equal Pairs : ",num)