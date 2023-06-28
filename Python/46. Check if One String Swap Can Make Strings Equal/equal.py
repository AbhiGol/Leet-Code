def can_strings_be_equal(s1, s2):
    
    if len(s1) != len(s2):
        return False

    differing_chars = []
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            differing_chars.append((s1[i], s2[i]))

        if len(differing_chars) > 2:
            return False

    if len(differing_chars) != 2:
        return False

    return differing_chars[0] == differing_chars[1][::-1]


s1 = "attack"
s2 = "defend"
print(can_strings_be_equal(s1, s2))  