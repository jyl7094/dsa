def selection_sort(lst):
    if type(lst) != list:
        return TypeError
    length = len(lst)
    for i in range(length-1):
        smallest = lst[i]
        found = i
        for j in range(i+1,length):
            if lst[j] < smallest:
                smallest = lst[j]
                found = j
        lst[found] = lst[i]
        lst[i] = smallest
    return lst
