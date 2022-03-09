def find_factorial_recursive(n): # time complexity: O(n)
    if n <= 1:
        return 1
    return n * find_factorial_recursive(n-1)

def find_factorial_iterative(n): # time complexity: O(n)
    ans = 1
    for i in range(n, 0, -1):
        ans *= i
    return ans
