fibonacci_cache = {}


def fibonacci(n):
    """Return the n'th term of the fibonacci sequence"""
    value = 0
    # First check if value in cache
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    # Produce fibonacci numbers
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    # Cache the value and return it
    fibonacci_cache[n] = value
    return value


for x in range(400):
    print(x, ":", fibonacci(x))
