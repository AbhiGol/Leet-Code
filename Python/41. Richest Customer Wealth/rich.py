accounts = [[2,8,7],[7,1,3],[1,9,5]]
rich = []

for i in range(0,len(accounts)):
    rich.append(sum(accounts[i]))
print(max(rich))