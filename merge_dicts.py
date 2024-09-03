def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()  # Start with a copy of the first dictionary
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value  # Sum the values if the key exists in both dictionaries
        else:
            merged_dict[key] = value  # Add the key-value pair if the key is only in the second dictionary
    return merged_dict

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

merged = merge_dicts(dict1, dict2)
print(merged)
