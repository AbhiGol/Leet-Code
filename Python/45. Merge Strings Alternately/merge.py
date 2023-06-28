word1 = "abcde"
word2 = "12345"
merge = []
i = 0

while len(merge) != len(word1) + len(word2):
    merge.append(word1[i])
    merge.append(word2[i])
    i += 1

print("".join(merge))