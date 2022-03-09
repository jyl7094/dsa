def fibonacci_iterative(n): # O(n)
    if n < 0:
        return False
    elif n < 2:
        return n
    else:
        a = 1
        b = 1
        for i in range(2, n):
            a, b = b+a, a
        return a


def fibonacci_recursive(n): # O(2^n)
    if n < 0: 
        return False
    elif n < 2: 
        return n
    else:
        return fibonacci_recursive(n-2) + fibonacci_recursive(n-1)

print(fibonacci_recursive(2) == fibonacci_recursive(2))