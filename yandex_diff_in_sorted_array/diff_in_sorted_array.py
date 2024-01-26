def get_first_minus_second_sorted_arrays(arr1: list, arr2: list):
    res_lst = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):

        if arr1[i] < arr2[j]:
            res_lst.append(arr1[i])
            i += 1

        elif arr1[i] > arr2[j]:
            j += 1

        else:
            i += 1

    if i < len(arr1):
        res_lst.extend(arr1[i:])

    return res_lst


