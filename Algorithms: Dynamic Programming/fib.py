def fib(): # Time complexity: O(n)
    cache = {} # Space complexity: O(n)
    def fibonacci(n):
        if n < 0:
            raise ValueError
        elif n in cache:
            return cache[n]
        else:
            if n < 2:
                return n
            else:
                cache[n] = fibonacci(n-1) + fibonacci(n-2)
                return cache[n]
    return fibonacci

def fib_bottom_up(n):
    cache = [0, 1]
    for i in range(2, n+1):
        cache.append(cache[i-2] + cache[i-1])
    return cache.pop()
