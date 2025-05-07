# 1- #
def flatten(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list

input_list = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
output = flatten(input_list)
print(output)

###################################################################################################

# 2- #
def reverse_nested(lst):
    if isinstance(lst, list):
        return [reverse_nested(item) for item in lst[::-1]]
    else:
        return lst
    
input_list = [[1, 2], [3, 4], [5, 6, 7]]
output = reverse_nested(input_list)
print(output)