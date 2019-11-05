
def is_one_away(s1, s2):
    mapping = {}
    if abs(len(s1) - len(s2)) > 1:
        return False
    elif len(s1) == len(s2):
        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
        if count > 1:
            return False
    else:
        if len(s1) < len(s2):
            temp = s1
            s1 = s2
            s2 = temp
        count = 0
        idx1 = 0
        idx2 = 0
        while idx1 < len(s1) and idx2 < len(s2):
            print(idx1, idx2)
            if s1[idx1] != s2[idx2]:
                count += 1
            else:
                idx2 += 1
            idx1 += 1
        if count > 1:
            return False

    return True

str2 = 'abcd'
str1 = 'bcd'

print(is_one_away(str1, str2))