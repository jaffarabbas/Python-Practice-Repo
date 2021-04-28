

def flatten_list(_2d_list):
    flat_list = []
    # Iterate through the outer list
    for element in _2d_list:
        if type(element) is list:
            # If the element is of type list, iterate through the sublist
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list

nested_list = [
[2,4,3,5],
[7,10,3,9],
[1,15,12],
]
newsort = flatten_list(nested_list)
newsort.sort()
print('Transformed Flat List',newsort)

