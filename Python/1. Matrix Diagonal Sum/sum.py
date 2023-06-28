matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(matrix)

sum = 0

for i in range(len(matrix)):
    sum = sum + matrix[i][i]
    sum = sum + matrix[i][len(matrix)-1-i]
    
if len(matrix) %2 == 1:
    sum = sum - matrix[len(matrix)//2][len(matrix)//2]
    print(sum)
else:
    print(sum)

