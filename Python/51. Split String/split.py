txt = "helloworld"
a = len(txt)/2
x = txt[:int(a)]
y = txt[int(a):len(txt)]
sp1count = 0
sp2count = 0
vowels = 'A','E','I','O','U','a','e','i','o','u'

for i in range(0,len(x)):
    for j in range(0,len(vowels)):
        if x[i] == vowels[j]:
            sp1count += 1
        if y[i] == vowels[j]:
            sp2count += 1
if sp1count == sp2count:
    print("True")
else:
    print("False")
