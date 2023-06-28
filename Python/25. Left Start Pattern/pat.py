num = 5
for i in range(1,num+1):
    for j in range(num+1,i,-1):
        print(" ",end=" ")
    for l in range(0,i):
        print("*",end=" ")
    print("\n")

for i in range(num-1,0,-1):
    for j in range(num+1,i,-1):
        print(" ",end=" ")
    for l in range(0,i):
        print("*",end=" ")
    print("\n")