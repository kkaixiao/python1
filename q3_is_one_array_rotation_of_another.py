
def is_rotation(lst1, lst2):
    if (not lst1) and (not lst2):
        return True
    elif (not lst1) or (not lst2):
        return False
    if len(lst1) != len(lst2):
        return False
    try:
        start_idx_lst2 = lst2.index(lst1[0])
    except ValueError:
        return False

    if start_idx_lst2 < 0:
        return False
    len_lists = len(lst1)
    for idx in range(1, len_lists):
        match_idx_lst2 = (idx + start_idx_lst2) % len_lists
        if lst1[idx] != lst2[match_idx_lst2]:
            return False
    return True


A = [1,2,3,4,5,6,7]
B = [4,5,6,7,1,2,3]

print(is_rotation(A, B))