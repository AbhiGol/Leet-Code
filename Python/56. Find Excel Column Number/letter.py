def excel_column_number(STR):
    result = 0
    n = len(STR)

    for i in range(n-1, -1, -1):
        c = STR[i]
        value = ord(c) - ord('A') + 1
        result += value * (26 ** (n - i - 1))

    return result

column_title = "AB"
column_number = excel_column_number(column_title)
print(column_number)