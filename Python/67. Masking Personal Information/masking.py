S = "AB@qq.com"

if '@' in S:
    S = S.lower()
    firstChar = S[0]
    asterix = S.find('@')
    print(S[0] + "*****" + S[asterix-1:])
else:
    S = S.replace('+', "")
    S = S.replace('(', '')
    S = S.replace('-', '')
    S = S.replace(')', '')
    S = S.replace(' ', '')
               
    if len(S) == 10:
        print("***-***-" + S[-4:])
    else:
        countryCode = len(S) - 10
        result = "+"
        for index in range(countryCode):
            result += "*"
        print(result + "-***-***-" + S[-4:])