
def common_elements_in_two_arrays(lst1, lst2):
    if (not lst1) or (not lst2):
        return []
    long_list, short_list = [], []
    if len(lst1) > len(lst2):
        long_list = lst1
        short_list = lst2

    else:
        long_list = lst2
        short_list = lst1

    return_list = []
    for item in long_list:
        if item in short_list:
            return_list.append(item)
    return return_list



A=[1,3,4,6,7,9]
B=[1,2,4,5,9,10,11]

print(common_elements_in_two_arrays(A, B))