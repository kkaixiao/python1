
def most_frequent_item(lst):
    if not lst:
        return None

    mapping_dict = {}

    for item in lst:
        if item not in mapping_dict:
            mapping_dict[item] = 1
        else:
            mapping_dict[item] += 1

    max_val = 0
    for k,v in mapping_dict.items():
        max_val = max(max_val, v)

    ret_val = -1
    for k,v in mapping_dict.items():
        if v == max_val:
            ret_val = k


    print(ret_val)

most_frequent_item([3,3,1,3,2,1])