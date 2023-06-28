n = 7
m = 1
for i in range(n,0,-1):
    for j in range(0,i):
        print(m,end=" ")
    m += 1
    print("\n")