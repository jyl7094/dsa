def quick_sort(lst, left, right):
    if type(lst) != list:
        raise TypeError
    if left < right:
        pivot = lst[right]
        idx = left - 1
        for i in range(left, right):
            if lst[i] < pivot:
                idx += 1
                lst[idx], lst[i] = lst[i], lst[idx]
        idx += 1
        lst[idx], lst[right] = lst[right], lst[idx]
        quick_sort(lst, left, idx-1)
        quick_sort(lst, idx+1, right)
        return lst
