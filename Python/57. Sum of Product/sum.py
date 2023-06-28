def sumOrProduct(n, q):
    sum = 0
    pro = 1
    if q == 1:
        for i in range(1,n+1):
           sum += i
        print(sum) 
    else:
        for i in range(1,n+1):
           pro *= i
        print(pro) 

sumOrProduct(15,2)