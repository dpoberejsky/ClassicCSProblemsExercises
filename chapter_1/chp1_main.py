from imports import *

def fib_recur(n: int) -> int:
    #Simple recursive function for finding fib numbers
    if n <= 2:
        return n
    return fib_recur(n-1) + fib_recur(n-2)



memo = {0: 0, 1:1}
def fib_memo(n: int) -> int:
    #Recursive function using memoization to speed up processing
    if n not in memo.keys():
        memo[n] = fib_memo(n-2) + fib_memo(n-1)
    return memo[n]

#Python auto caching
from functools import lru_cache
@lru_cache(maxsize=None)
def fib_memo_auto(n: int) -> int:
    if n < 2:
        return n
    return fib_memo_auto(n-2) + fib_memo_auto(n-1)

#Tuple unpacking
def fib_tuple(n: int) -> int:
    if n == 0: return n
    last = 0
    next = 1
    for _ in range(1, n):
        last, next = next, last+next
    return next
