

def non_repeating(s):
    if not s:
        return None
    if len(s) <= 1:
        return s[0]
    mapping = {}
    for char in s:
        if char not in mapping:
            mapping[char] = 1
        else:
            mapping[char] = mapping[char] + 1

    for k, v in mapping.items():
        if v == 1:
            return k


str1 = 'ccaada'


print(non_repeating(str1))
