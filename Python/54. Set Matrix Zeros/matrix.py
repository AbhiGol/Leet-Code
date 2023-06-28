matrix = [ [99,17,67,46], [0,87,32,53], [27,24,79,71], [23,0,17,0], [85,100,40,0] ]
row = []
column = []

for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            if matrix[i][j] == 0:
                row.append(i)
                column.append(j)


print(*set(row))
print(*set(column))

for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            for k in range(0,len(row)):
                if i == row[k]:
                    matrix[i][j] = 0
            for l in range(0,len(column)):
                if j == column[l]:
                    matrix[i][j] = 0

print(matrix)