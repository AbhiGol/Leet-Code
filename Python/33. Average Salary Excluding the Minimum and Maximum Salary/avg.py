salary = [4000,3000,1000,2000]
avg = 0
count = 0
salary.sort()
for i in range(1,len(salary)-1):
    avg = avg + salary[i]
    count += 1
print(avg/count)