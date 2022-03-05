# merge sort
# assuming both lists only contain ints and at least one is not empty
def merge_sorted_arrays(a, b):
    lst = []
    i, j = 0, 0

    if not a or not b:
        return a+b # O(n)
    
    while i < len(a) and j < len(b): # O(n)
        if a[i] >= b[j]:
            lst.append(b[j])
            j += 1
        else:
            lst.append(a[i])
            i += 1
    
    return lst+a[i:]+b[j:] # O(n)


# assert merge_sorted_arrays([0,3,4,31], [4,6,30]) == [0, 3, 4, 4, 6, 30, 31]
print(merge_sorted_arrays([0,3,4,31], [4,6,30]))