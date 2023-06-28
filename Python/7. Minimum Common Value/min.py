num1 = [2,3,4,5]
num2 = [5,2,3,4,7]

num1.sort()
num2.sort()

for i in range(0,len(num1)):
    for j in range(0,len(num2)):
        if num1[i] == num2[j]:
            print(num1[i])
        break