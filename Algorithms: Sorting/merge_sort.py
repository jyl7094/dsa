def merge(left, right):
    output = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
    while i < len(left):
        output.append(left[i])
        i += 1
    while j < len(right):
        output.append(right[j])
        j += 1
    return output

def merge_sort(lst):
    if type(lst) != list:
        raise TypeError
    if len(lst) == 1:
        return lst
    div = len(lst) // 2
    left = lst[:div]
    right = lst[div:]
    return merge(merge_sort(left), merge_sort(right))
