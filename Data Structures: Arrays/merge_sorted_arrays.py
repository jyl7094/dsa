# merge sort
# assuming both lists only contain ints and at least one is not empty
def merge_sorted_arrays(a, b):
    if not a or not b:
        a += b  # O(n)
        return a
    
    lst = []
    i, j = 0, 0

    while i < len(a) and j < len(b): # O(n)
        if a[i] <= b[j]:
            lst.append(a[i])
            i += 1
        else:
            lst.append(b[j])
            j += 1
    
    lst += a[i:] + b[j:] # O(n)
    return lst
