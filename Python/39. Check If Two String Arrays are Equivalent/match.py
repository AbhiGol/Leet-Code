word1 = ["a", "cb"]
word2 = ["ab", "c"]
sep = ""
joinstring1 = sep.join(word1)
joinstring2 = sep.join(word2)

if joinstring1 == joinstring2:
    print("True")
else:
    print("False")