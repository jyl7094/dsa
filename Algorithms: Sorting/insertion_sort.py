def insertion_sort(lst):
    if type(lst) != list:
        raise TypeError
    for step in range(len(lst)):
        key = lst[step]
        i = step - 1
        while i >= 0 and lst[i] > key:
            lst[i + 1] = lst[i]
            i = i - 1
        lst[i + 1] = key
    return lst
