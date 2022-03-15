def first_recurring_character(lst):
    d = {}
    for elem in lst:
        if elem not in d:
            d[elem] = 1
        else:
            return elem
    return None
