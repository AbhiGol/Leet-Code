ranks = [13,3,3,2,3]
suits = ["b","a","a","a","a"]
countrank = 0
countsuits = 0

for i in range(0,len(ranks)):
    for j in range(i+1,len(ranks)):
        if ranks[i] == ranks[j]:
            countrank += 1
    if suits[0] == suits[i]:
        countsuits +=1

if countsuits == 5:
    print("Flush")
elif countrank == 3:
    print("Three of a Kind")
elif countrank == 2:
    print("Pair")
elif countrank == 0:
    print("High Card")