arr = [2]
n = 1
k = 2
count = 0
firstposition = 0
secondposition = 0

for i in range(0,n):
    if arr[i] == k:
        firstposition = i
        count += 1
        break
for i in range(n-1,0,-1):
    if arr[i] == k:
        secondposition = i   
        count += 1
        break
#print(firstposition,secondposition)

if count == 0:
    print("-1","-1")
else:
    print(firstposition,secondposition)