def bubble_sort(lst):
    if type(lst) != list:
        raise TypeError
    length = len(lst)
    for _ in range(length):
        for i in range(length-1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst
