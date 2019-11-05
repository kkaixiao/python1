
def common_elements_in_two_arrays(lst1, lst2):
    if (not lst1) or (not lst2):
        return []
    result = []
    p1, p2 = 0, 0
    while p1 < len(lst1) and p2 < len(lst2):

        if lst1[p1] == lst2[p2]:
            result.append(lst1[p1])
            p1 += 1
            p2 += 1
        elif lst1[p1] > lst2[p2]:
            p2 += 1
        else:
            p1 += 1
    return result


A=[1,3,4,6,7,9]
B=[1,2,4,5,9,10,12]

print(common_elements_in_two_arrays(A, B))