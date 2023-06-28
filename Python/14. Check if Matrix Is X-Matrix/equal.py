grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]
count = 0
count1 = 0

for i in range(0,len(grid[0])):
    for j in range(0,len(grid[0])):
        if ((i==j) or (i+j) == (len(grid)-1)):
            if grid[i][j] != 0:
                count += 1
        elif i != j:
            if grid[i][j] == 0:
                count1 +=1