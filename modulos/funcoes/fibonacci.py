from functools import lru_cache


# memoize
# memoization
@lru_cache(maxsize=512)
def fib(x):
    if x in [0, 1]:
        return x
    return fib(x - 1) + fib(x - 2)
