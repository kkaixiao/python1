
def most_frequent_item(lst):
    if not lst:
        return None

    mapping_dict = {}
    max_count, max_item = -1, None

    for item in lst:
        if item not in mapping_dict:
            mapping_dict[item] = 1
        else:
            mapping_dict[item] += 1
        if max_count < mapping_dict[item]:
            max_count = mapping_dict[item]
            max_item = item

    return max_item

print(most_frequent_item([3,1,1,3,2,3]))